import math
from OpenGL.GL import *
import sys
import glfw

SCREEN_SIZE  = width,height = 800,600

angle=60.0
pov = 0.0
h = math.sqrt(3)/2

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
    
    # Reset modelview matrix and set up camera
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    from OpenGL.GLU import gluLookAt
    gluLookAt(0.0, 2.0, 5.0,  # Camera position
              0.0, 0.0, 0.0,  # Look at point
              0.0, 1.0, 0.0)  # Up vector

    glRotatef(pov, 0.0, 1.0, 0.0)  # Rotate around Y axis
    
    # Define tetrahedron vertices
    # A tetrahedron has 4 vertices and 4 triangular faces
    v1 = [0.0, 1.0, 0.0]      # Top vertex
    v2 = [-1.0, -1.0, 1.0]    # Front-left
    v3 = [1.0, -1.0, 1.0]     # Front-right
    v4 = [0.0, -1.0, -1.0]    # Back
    
    glBegin(GL_TRIANGLES)
    
    # Face 1: Front (v1, v2, v3) - Green
    glColor3f(0.0, 0.8, 0.2)
    glVertex3fv(v1)
    glVertex3fv(v3)
    glVertex3fv(v2)
    
    # Face 2: Left (v1, v4, v2) - Red
    glColor3f(0.8, 0.1, 0.0)
    glVertex3fv(v1)
    glVertex3fv(v2)
    glVertex3fv(v4)
    
    # Face 3: Right (v1, v3, v4) - Blue
    glColor3f(0.2, 0.2, 1.0)
    glVertex3fv(v1)
    glVertex3fv(v4)
    glVertex3fv(v3)
    
    # Face 4: Bottom (v2, v3, v4) - Yellow
    glColor3f(0.9, 0.9, 0.1)
    glVertex3fv(v2)
    glVertex3fv(v3)
    glVertex3fv(v4)
    
    glEnd()


window=init()

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


while not glfw.window_should_close(window):
    # Render here, e.g. using pyOpenGL
    draw()
    pov += 0.1
    # Swap front and back buffers
    glfw.swap_buffers(window)

    # Poll for and process events
    glfw.poll_events()
    if vp_size_changed:
        vp_size_changed = False
        w, h = glfw.get_framebuffer_size(window)
        glViewport(0, 0, w, h)
glfw.terminate()