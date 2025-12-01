import math
from OpenGL.GL import *
import sys
import glfw

SCREEN_SIZE  = width,height = 800,600

angle=0.0
pov = 0.0
TRI_HEIGHT_RATIO = math.sqrt(3)/2  # Height ratio for equilateral triangle

vp_size_changed = False

# Define a simple function to create ctypes arrays of floats:
def vec(*args):
    return (GLfloat * len(args))(*args)

def resize_cb(window, w, h):
    global vp_size_changed
    vp_size_changed = True

def init():
    if not glfw.init():
        print("Unable to get window")
        sys.exit(1)
    
    # Use compatibility profile to support legacy OpenGL functions
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 2)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 1)

    window = glfw.create_window(640, 480, "Tetraedro", None, None)
    if not window:
        glfw.terminate()
        sys.exit(1)
    
    # Make the window's context current
    glfw.make_context_current(window)
    glfw.set_window_size_callback(window, resize_cb)
    return window

def draw():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    print(f"  Current angle: {angle:.1f}°")
    # Reset modelview matrix and set up camera
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    from OpenGL.GLU import gluLookAt
    gluLookAt(0.0, 1.5, 4.0,  # Camera position
              0.0, 0.0, 0.0,  # Look at origin
              0.0, 1.0, 0.0)  # Up vector (Y is up)

    glRotatef(pov, 0.0, 1.0, 0.0)  # Rotate around Y axis
    
    # Calculate the rotation angle for unfolding
    # When angle=0, faces are flat (180°)
    # When angle=70.53, faces form closed tetrahedron
    rotation = 180 - angle  # Angle from vertical
    
    # Size of triangle - much smaller to fit in view
    size = 1.4
    height_tri = size * TRI_HEIGHT_RATIO  # Height of equilateral triangle
    
    glBegin(GL_TRIANGLES)
    
    # BOTTOM FACE (base) - Yellow - horizontal on XZ plane
    glColor3f(0.9, 0.9, 0.1)
    glVertex3f(-size/2, 0.0, height_tri/3)
    glVertex3f(size/2, 0.0, height_tri/3)
    glVertex3f(0.0, 0.0, -2*height_tri/3)
    
    
    # FRONT FACE - Green
    glColor3f(0.0, 0.8, 0.2)
    # Rotate around front edge (X-axis at z = height_tri/3)
    glVertex3f(-size/2, 0.0, height_tri/3)
    glVertex3f(size/2, 0.0, height_tri/3)
    # Third vertex rotates backward from the edge
    glVertex3f(0.0, 
               height_tri * math.sin(math.radians(rotation)), 
               height_tri/3 - height_tri * math.cos(math.radians(rotation)))
    
    # LEFT FACE - Red  
    glColor3f(0.8, 0.1, 0.0)
    # Rotate around left edge (from back-left to front-left)
    # Edge from (0, 0, -2*height_tri/3) to (-size/2, 0, height_tri/3)
    glVertex3f(0.0, 0.0, -2*height_tri/3)
    glVertex3f(-size/2, 0.0, height_tri/3)
    
    # Calculate third vertex rotation
    # Edge vector and perpendicular rotation
    edge_len = size  # Length of edge
    # The third vertex is at the centroid offset, rotating around the left edge
    # Base position when flat (angle=0): (size/2, 0, -height_tri/3)
    # Edge midpoint: (-size/4, 0, -height_tri/6)
    # Perpendicular direction from edge to third vertex when flat
    perp_dist = height_tri  # Distance from edge to opposite vertex
    
    # Edge direction (normalized)
    edge_dx = -size/2
    edge_dz = height_tri
    edge_length = math.sqrt(edge_dx**2 + edge_dz**2)
    edge_dx /= edge_length
    edge_dz /= edge_length
    
    # Perpendicular in XZ plane (rotate edge vector 90° clockwise in XZ)
    perp_x = edge_dz
    perp_z = -edge_dx
    
    # Midpoint of edge
    mid_x = -size/4
    mid_z = -height_tri/6
    
    # Rotated position
    rx = mid_x + perp_x * perp_dist * math.cos(math.radians(rotation))
    ry = perp_dist * math.sin(math.radians(rotation))
    rz = mid_z + perp_z * perp_dist * math.cos(math.radians(rotation))
    glVertex3f(rx, ry, rz)
    
    # RIGHT FACE - Blue
    glColor3f(0.2, 0.2, 1.0)
    # Rotate around right edge (from back-center to front-right)
    # Edge from (0, 0, -2*height_tri/3) to (size/2, 0, height_tri/3)
    glVertex3f(0.0, 0.0, -2*height_tri/3)
    glVertex3f(size/2, 0.0, height_tri/3)
    
    # Calculate third vertex rotation (mirror of left face)
    # Edge direction (normalized)
    edge_dx = size/2
    edge_dz = height_tri
    edge_length = math.sqrt(edge_dx**2 + edge_dz**2)
    edge_dx /= edge_length
    edge_dz /= edge_length
    
    # Perpendicular in XZ plane (rotate edge vector 90° counter-clockwise in XZ)
    perp_x = -edge_dz
    perp_z = edge_dx
    
    # Midpoint of edge
    mid_x = size/4
    mid_z = -height_tri/6
    
    # Rotated position
    rx = mid_x + perp_x * perp_dist * math.cos(math.radians(rotation))
    ry = perp_dist * math.sin(math.radians(rotation))
    rz = mid_z + perp_z * perp_dist * math.cos(math.radians(rotation))
    glVertex3f(rx, ry, rz)
    
    glEnd()



auto_rotate = True

def key_callback(window, key, scancode, action, mods):
    global angle, auto_rotate
    if action == glfw.PRESS or action == glfw.REPEAT:
        if key == glfw.KEY_UP:
            angle += 2.0  # Unfold more
        elif key == glfw.KEY_DOWN:
            angle -= 2.0  # Fold more
        elif key == glfw.KEY_SPACE:
            auto_rotate = not auto_rotate  # Toggle rotation
        elif key == glfw.KEY_R:
            angle = 0.0  # Reset to default
        
        # Clamp angle between 0 and 70.53
        angle = max(0.0, min(110, angle))

window=init()
glfw.set_key_callback(window, key_callback)

lightpos = vec(20, 20, 1, 0)
red = vec(0.8, 0.1, 0.0, 1.0)
green = vec(0.0, 0.8, 0.2, 1.0)
blue = vec(0.2, 0.2, 1.0, 1.0)

# Set up OpenGL state
glClearColor(0.2, 0.2, 0.2, 1.0)  # Gray background instead of black
glEnable(GL_DEPTH_TEST)  # Enable depth testing for 3D

# Ensure we're rendering filled polygons, not wireframe
glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)

# Disable backface culling so we can see all faces
glDisable(GL_CULL_FACE)

# Set up projection matrix
glMatrixMode(GL_PROJECTION)
glLoadIdentity()
# Set up perspective projection (fov, aspect, near, far)
w, h = glfw.get_framebuffer_size(window)
aspect = w / h if h > 0 else 1.0
from OpenGL.GLU import gluPerspective
gluPerspective(45.0, aspect, 0.1, 100.0)

# Set up modelview matrix
glMatrixMode(GL_MODELVIEW)
glLoadIdentity()

print("Controls:")
print("  UP/DOWN arrows: Unfold/Fold the tetrahedron")
print("  SPACE: Toggle auto-rotation")
print("  R: Reset angle")
print(f"  Current angle: {angle:.1f}° (0° = flat, 70.53° = closed)")

while not glfw.window_should_close(window):
    # Render here, e.g. using pyOpenGL
    draw()
    if auto_rotate:
        pov += 0.3
    # Swap front and back buffers
    glfw.swap_buffers(window)

    # Poll for and process events
    glfw.poll_events()
    if vp_size_changed:
        vp_size_changed = False
        w, h = glfw.get_framebuffer_size(window)
        glViewport(0, 0, w, h)
glfw.terminate()