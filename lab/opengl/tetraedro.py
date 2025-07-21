import math
from OpenGL.GL import *
import sys
import glfw

SCREEN_SIZE  = width,height = 800,600

angle=0
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
    
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 2)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 1)
    #glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, GL_TRUE)
    #glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)
    glfw.window_hint(glfw.OPENGL_DEBUG_CONTEXT, GL_TRUE)

    window = glfw.create_window(640, 480, "Utah teapot", None, None)
    if not window:
        glfw.terminate()
        sys.exit(1)
    
    # Make the window's context current
    glfw.make_context_current(window)
    glfw.set_window_size_callback(window, resize_cb)
    return window


def triangleFace():
    glBegin(GL_TRIANGLES)
    glVertex3f(-0.5, h, 1.0)    
    glVertex3f(0.5, h, 1.0)
    glVertex3f(0.0, 0.0, 1.0)
    
    glEnd()

def draw():
    print(angle,pov)

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0)

    glRotatef (pov, 0.0, 1.0, 1.0)
    
    glPushMatrix()
    triangleFace()
    #glTranslatef (2.0, 0.0, 0.0);

    glRotatef (60, 0.0, 0.0, 1.0);
    glRotatef (-angle, 0.5, h, 0.0);

    triangleFace()

    glPopMatrix()
    glPushMatrix();

    glRotatef (-60, 0.0, 0.0, 1.0);
    glRotatef (angle, -0.5, h, 0.0);

    triangleFace()
    glPopMatrix()
    glPushMatrix();

    glTranslatef (0.5, h, 0.0);
    glRotatef (60, 0.0, 0.0, 1.0);
    glRotatef (angle, -0.5, h, 0.0);

    triangleFace()
    glPopMatrix()


    
window=init()

lightpos = vec(20, 20, 1, 0)
red = vec(0.8, 0.1, 0.0, 1.0)

green = vec(0.0, 0.8, 0.2, 1.0)
blue = vec(0.2, 0.2, 1.0, 1.0)

glClearColor(0.0, 0.0, 0.0, 0.0)

glEnable(GL_DEPTH_TEST)

lightpos = vec(0, 0, 1, 0)  # Move light into the camera's view
#glLight(GL_LIGHT0, GL_POSITION, lightpos)

while not glfw.window_should_close(window):
    # Render here, e.g. using pyOpenGL
    draw()
    # Swap front and back buffers
    glfw.swap_buffers(window)

    # Poll for and process events
    glfw.poll_events()
    if vp_size_changed:
        vp_size_changed = False
        w, h = glfw.get_framebuffer_size(window)
        glViewport(0, 0, w, h)
glfw.terminate()