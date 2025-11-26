#!/usr/bin/env python3
# particles_physics.py
# GPU-accelerated particle physics demo (numba.cuda + pygame)
#
# Modes:
#  - 'fast'    : gravity, damping, wall collisions (scales to large N)
#  - 'collide' : adds simple pairwise elastic collisions (O(N^2), only for small N)

from numba import cuda
import numpy as np
import pygame, sys, math, time

# Window size
W, H = 1440, 960

# Number of particles
NUMBER_OF_PARTICLES = 15000   # reduce if using 'collide' mode
#MODE = 'fast'                 # 'fast' or 'collide'
MODE = 'collide'

# Physics params
DT = 0.005
GRAVITY = 200.0               # pixels / s^2 downward (scaled)
DAMPING = 0.999               # velocity damping per step
PARTICLE_RADIUS = 2.0         # pixel radius for collision tests
ELASTICITY = 0.9              # bounce restitution when hitting walls
MASS = 1.0

# GPU kernel config
THREADS_PER_BLOCK = 128

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("GPU Particle Physics")
screen.fill(pygame.Color('black'))

# initial positions (spread across screen), velocities random
rng = np.random.RandomState(1234)
x = (rng.random(NUMBER_OF_PARTICLES) * W).astype(np.float32)
y = (rng.random(NUMBER_OF_PARTICLES) * H).astype(np.float32)
vx = (rng.normal(0, 40, NUMBER_OF_PARTICLES)).astype(np.float32)
vy = (rng.normal(0, 30, NUMBER_OF_PARTICLES)).astype(np.float32)
radius = np.full(NUMBER_OF_PARTICLES, PARTICLE_RADIUS, dtype=np.float32)
mass = np.full(NUMBER_OF_PARTICLES, MASS, dtype=np.float32)

# precompute colors
indices = np.arange(NUMBER_OF_PARTICLES)
colors = np.zeros((NUMBER_OF_PARTICLES, 3), dtype=np.uint8)
colors[:, 0] = (indices * 37) % 255
colors[:, 1] = (indices * 97) % 255
colors[:, 2] = (indices * 53) % 255

# device arrays
d_x = cuda.to_device(x)
d_y = cuda.to_device(y)
d_vx = cuda.to_device(vx)
d_vy = cuda.to_device(vy)
d_radius = cuda.to_device(radius)
d_mass = cuda.to_device(mass)

# mouse attractor state (host-side)
mouse_x = np.array([W//2], dtype=np.float32)
mouse_y = np.array([H//2], dtype=np.float32)
mouse_strength = np.array([0.0], dtype=np.float32)  # 0 => off, positive attract, negative repel

d_mouse_x = cuda.to_device(mouse_x)
d_mouse_y = cuda.to_device(mouse_y)
d_mouse_strength = cuda.to_device(mouse_strength)

# Fast kernel: gravity, damping, and wall collisions
@cuda.jit
def step_kernel_fast(x, y, vx, vy, dt, gravity, damping, width, height, elasticity):
    i = cuda.grid(1)
    if i >= x.size:
        return

    # acceleration: gravity only (downwards)
    ax = 0.0
    ay = gravity

    # integrate (semi-implicit Euler)
    vx[i] += ax * dt
    vy[i] += ay * dt

    # apply damping
    vx[i] *= damping
    vy[i] *= damping

    # update position
    x[i] += vx[i] * dt
    y[i] += vy[i] * dt

    # simple wall collisions (reflect & apply elasticity)
    r = 1.0  # small effective radius (we render slightly larger if needed)
    if x[i] < r:
        x[i] = r
        vx[i] = -vx[i] * elasticity
    elif x[i] > width - r:
        x[i] = width - r
        vx[i] = -vx[i] * elasticity

    if y[i] < r:
        y[i] = r
        vy[i] = -vy[i] * elasticity
    elif y[i] > height - r:
        y[i] = height - r
        vy[i] = -vy[i] * elasticity

# Collision kernel: pairwise elastic collisions (O(N^2)) — only use for small N
@cuda.jit
def step_kernel_collide(x, y, vx, vy, radius, mass, dt, gravity, damping, width, height, elasticity):
    i = cuda.grid(1)
    n = x.size
    if i >= n:
        return

    ax = 0.0
    ay = gravity

    # integrate velocity by external forces
    vx[i] += ax * dt
    vy[i] += ay * dt

    # damping
    vx[i] *= damping
    vy[i] *= damping

    # basic position update
    x[i] += vx[i] * dt
    y[i] += vy[i] * dt

    # wall collisions
    r = radius[i]
    if x[i] < r:
        x[i] = r
        vx[i] = -vx[i] * elasticity
    elif x[i] > width - r:
        x[i] = width - r
        vx[i] = -vx[i] * elasticity
    if y[i] < r:
        y[i] = r
        vy[i] = -vy[i] * elasticity
    elif y[i] > height - r:
        y[i] = height - r
        vy[i] = -vy[i] * elasticity

    # pairwise collision check: naive O(N^2)
    # each thread i checks collisions with j > i to avoid double-handling (but we still try to update both; beware race conditions).
    # For simplicity we only resolve using a symmetric impulse computed per pair; this can still cause some race artifacts but
    # works reasonably for small N in demo settings.
    xi = x[i]
    yi = y[i]
    vxi = vx[i]
    vyi = vy[i]
    ri = radius[i]
    mi = mass[i]

    for j in range(n):
        if j == i:
            continue
        xj = x[j]
        yj = y[j]
        dx = xj - xi
        dy = yj - yi
        dist2 = dx*dx + dy*dy
        # skip if farther than combined radii
        if dist2 <= 0.0:
            continue
        combined = ri + radius[j]
        if dist2 < combined*combined:
            dist = math.sqrt(dist2)
            # normal
            nx = dx / dist
            ny = dy / dist
            # relative velocity along normal
            rvx = vx[j] - vxi
            rvy = vy[j] - vyi
            rel = rvx * nx + rvy * ny
            if rel > 0:
                # already separating
                continue
            # compute impulse scalar (elastic collision)
            mj = mass[j]
            e = elasticity
            j_impulse = -(1 + e) * rel / (1/mi + 1/mj)
            # impulse vector
            ix = j_impulse * nx
            iy = j_impulse * ny
            # apply to i and j (note: this writes vx/vy for both; possible race conditions if both threads write same j)
            vxi -= ix / mi
            vyi -= iy / mi
            # write back to vx/vy for j in a non-atomic way (race possible). This is demonstration-quality.
            vx[j] += ix / mj
            vy[j] += iy / mj
            # positional correction (simple push)
            overlap = combined - dist
            if overlap > 0:
                push = 0.5 * overlap
                x[i] -= nx * push
                y[i] -= ny * push
                # attempt to push j as well (may race)
                x[j] += nx * push
                y[j] += ny * push

    # write back the updated velocity for i
    vx[i] = vxi
    vy[i] = vyi

# Optional: mouse attractor kernel (adds force towards/away from mouse)
@cuda.jit
def mouse_kernel(x, y, vx, vy, mouse_x, mouse_y, strength, dt):
    i = cuda.grid(1)
    if i >= x.size:
        return
    sx = mouse_x[0]
    sy = mouse_y[0]
    s = strength[0]
    if s == 0.0:
        return
    dx = sx - x[i]
    dy = sy - y[i]
    dist2 = dx*dx + dy*dy + 1e-6
    inv = 1.0 / math.sqrt(dist2)
    # Force magnitude falloff ~ 1/dist
    f = s * inv
    vx[i] += f * dx * dt
    vy[i] += f * dy * dt

# Configure grid
blockspergrid = (NUMBER_OF_PARTICLES + (THREADS_PER_BLOCK - 1)) // THREADS_PER_BLOCK

# Main loop
clock = pygame.time.Clock()
running = True

# CPU view arrays for rendering
x_host = x
y_host = y

# Precompute surface pixel array with correct shape
for frame in range(1000000):
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
        elif event.type == pygame.MOUSEMOTION:
            mx, my = event.pos
            mouse_x[0] = float(mx)
            mouse_y[0] = float(my)
            d_mouse_x.copy_to_device(mouse_x)
            d_mouse_y.copy_to_device(mouse_y)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # left click attract, right click repel
            if event.button == 1:
                mouse_strength[0] = 6000.0
            elif event.button == 3:
                mouse_strength[0] = -6000.0
            d_mouse_strength.copy_to_device(mouse_strength)
        elif event.type == pygame.MOUSEBUTTONUP:
            mouse_strength[0] = 0.0
            d_mouse_strength.copy_to_device(mouse_strength)

    if not running:
        break

    # choose kernel
    if MODE == 'fast':
        step_kernel_fast[blockspergrid, THREADS_PER_BLOCK](
            d_x, d_y, d_vx, d_vy, DT, GRAVITY, DAMPING, W, H, ELASTICITY
        )
    else:
        # collision mode (slow)
        step_kernel_collide[blockspergrid, THREADS_PER_BLOCK](
            d_x, d_y, d_vx, d_vy, d_radius, d_mass, DT, GRAVITY, DAMPING, W, H, ELASTICITY
        )

    # apply mouse forces (optional)
    if mouse_strength[0] != 0.0:
        mouse_kernel[blockspergrid, THREADS_PER_BLOCK](
            d_x, d_y, d_vx, d_vy, d_mouse_x, d_mouse_y, d_mouse_strength, DT
        )

    # copy back for rendering
    d_x.copy_to_host(x_host)
    d_y.copy_to_host(y_host)

    # clear screen quickly
    screen.fill(pygame.Color('black'))

    # project to integer coordinates
    xp = x_host.astype(np.int32)
    yp = y_host.astype(np.int32)

    # mask in-bounds
    mask = (xp >= 0) & (xp < W) & (yp >= 0) & (yp < H)

    # draw into pixel array with surfarray for speed
    pixels = pygame.surfarray.pixels3d(screen)
    try:
        # draw each particle as a 2x2 square for visibility (clamp edges)
        idx = np.where(mask)[0]
        if idx.size:
            xp_valid = xp[idx]
            yp_valid = yp[idx]
            cols = colors[idx]
            # set the pixel and neighbors (be careful at edges)
            pixels[xp_valid, yp_valid] = cols
            # small safety checks to avoid out-of-bounds when adding +1
            inside_xp1 = xp_valid + 1 < W
            inside_yp1 = yp_valid + 1 < H
            both = inside_xp1 & inside_yp1
            if both.any():
                sel = idx[both]
                pixels[xp_valid[both]+1, yp_valid[both]] = colors[sel]
                pixels[xp_valid[both], yp_valid[both]+1] = colors[sel]
                pixels[xp_valid[both]+1, yp_valid[both]+1] = colors[sel]
    finally:
        del pixels

    pygame.display.flip()
    # cap to ~60 FPS (host rendering). GPU physics may iterate faster if you remove this.
    clock.tick(60)

pygame.quit()
sys.exit()
