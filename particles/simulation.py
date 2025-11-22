import pygame
from particle import Particle
import random

class Simulation:
    def __init__(self, width=800, height=600, num_particles=50):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Particle Simulation")
        self.clock = pygame.time.Clock()
        self.running = True
        
        self.particles = []
        for _ in range(num_particles):
            x = random.randint(20, width - 20)
            y = random.randint(20, height - 20)
            color = (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))
            self.particles.append(Particle(x, y, radius=random.randint(5, 15), color=color))

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                elif event.key == pygame.K_r:
                    self.__init__(self.width, self.height, len(self.particles)) # Reset

    def check_collisions(self):
        import math
        for i in range(len(self.particles)):
            for j in range(i + 1, len(self.particles)):
                p1 = self.particles[i]
                p2 = self.particles[j]
                
                dx = p2.x - p1.x
                dy = p2.y - p1.y
                distance = math.hypot(dx, dy)
                
                if distance < p1.radius + p2.radius:
                    # Collision detected
                    nx = dx / distance
                    ny = dy / distance
                    
                    # Tangent vector
                    tx = -ny
                    ty = nx
                    
                    # Dot product tangent
                    dpTan1 = p1.vx * tx + p1.vy * ty
                    dpTan2 = p2.vx * tx + p2.vy * ty
                    
                    # Dot product normal
                    dpNorm1 = p1.vx * nx + p1.vy * ny
                    dpNorm2 = p2.vx * nx + p2.vy * ny
                    
                    # Conservation of momentum in 1D
                    m1 = p1.mass
                    m2 = p2.mass
                    
                    mom1 = (dpNorm1 * (m1 - m2) + 2 * m2 * dpNorm2) / (m1 + m2)
                    mom2 = (dpNorm2 * (m2 - m1) + 2 * m1 * dpNorm1) / (m1 + m2)
                    
                    # Update velocities
                    p1.vx = tx * dpTan1 + nx * mom1
                    p1.vy = ty * dpTan1 + ny * mom1
                    p2.vx = tx * dpTan2 + nx * mom2
                    p2.vy = ty * dpTan2 + ny * mom2

                    # if velocity is small particle shold stop
                    if p1.vx < 0.000001 and p1.vy < 0.000001:
                        p1.vx = 0
                        p1.vy = 0
                    if p2.vx < 0.000001 and p2.vy < 0.000001:
                        p2.vx = 0
                        p2.vy = 0
                    
                    # Prevent sticking (overlap correction)
                    overlap = 0.5 * (p1.radius + p2.radius - distance + 1)
                    p1.x -= overlap * nx
                    p1.y -= overlap * ny
                    p2.x += overlap * nx
                    p2.y += overlap * ny

    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()
        
        for p in self.particles:
            if mouse_pressed[0]: # Left click to attract
                dx = mouse_pos[0] - p.x
                dy = mouse_pos[1] - p.y
                dist = max(1, (dx**2 + dy**2)**0.5)
                force = 0.5 # Attraction strength
                p.vx += (dx / dist) * force
                p.vy += (dy / dist) * force
            elif mouse_pressed[2]: # Right click to repel
                dx = mouse_pos[0] - p.x
                dy = mouse_pos[1] - p.y
                dist = max(1, (dx**2 + dy**2)**0.5)
                force = 0.5 # Repulsion strength
                p.vx -= (dx / dist) * force
                p.vy -= (dy / dist) * force
                
            p.move(gravity=0.000000000001, friction=1.0)
            p.check_boundaries(self.width, self.height)
        self.check_collisions()

    def draw(self):
        self.screen.fill((0, 0, 0))  # Black background
        for p in self.particles:
            p.draw(self.screen)
        pygame.display.flip()

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(60) # Limit to 60 FPS
        
        pygame.quit()
