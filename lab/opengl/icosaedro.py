import OpenGL
import math
from OpenGL.GL import *
import glfw
import sys

if not glfw.init():
    print("Unable to get window")
    sys.exit(1)

# Use compatibility profile to support legacy OpenGL functions
glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 2)
glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 1)

window = glfw.create_window(800, 600, "Tetraedro", None, None)
if not window:
    glfw.terminate()
    sys.exit(1)

# Make the window's context current
glfw.make_context_current(window)

vp_size_changed = False

angle=20
pov = 0.0
TRI_HEIGHT_RATIO = math.sqrt(3)/2  # Height ratio for equilateral triangle

# Define a simple function to create ctypes arrays of floats:
def vec(*args):
    return (GLfloat * len(args))(*args)

def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    #glShadeModel(GL_FLAT)
    pos1 = vec(2.0, 2.0, -5.0, 0.0)
    pos = vec(2.0, 2.0, 5.0, 0.0)
    red = vec(0.8, 0.1, 0.0, 1.0)
    green = vec(0.0, 0.8, 0.2, 1.0)
    blue = vec(0.2, 0.2, 1.0, 1.0)

    glLightfv(GL_LIGHT0, GL_POSITION, pos)
    glEnable(GL_CULL_FACE)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_DEPTH_TEST)

    glLightfv(GL_LIGHT1, GL_POSITION, pos1)
    glEnable(GL_LIGHT1)

def triangleFace():
    glBegin(GL_TRIANGLES)
    glVertex3f(0, 0, 0)
    glVertex3f(0.5, TRI_HEIGHT_RATIO, 0)
    glVertex3f(-0.5, TRI_HEIGHT_RATIO, 0)

    glEnd()

def on_draw():
    global angle,pov

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glColor3f(1.0, 0.0, 1.0)

    glRotatef (pov, 0.0, 1.0, 0.0)
    pov=0
    glPushMatrix()

    triangleFace()
    #glTranslatef (2.0, 0.0, 0.0)

    glRotatef (60, 0.0, 0.0, 1.0)
    glRotatef (-angle, 0.5, TRI_HEIGHT_RATIO, 0.0)

    triangleFace()

    glPopMatrix()
    glPushMatrix()

    glRotatef (-60, 0.0, 0.0, 1.0)
    glRotatef (angle, -0.5, TRI_HEIGHT_RATIO, 0.0)

    triangleFace()
    glPopMatrix()
    glPushMatrix()

    glTranslatef (0.5, TRI_HEIGHT_RATIO, 0.0)
    glRotatef (60, 0.0, 0.0, 1.0)
    glRotatef (angle, -0.5, TRI_HEIGHT_RATIO, 0.0)

    triangleFace()

    glPopMatrix()

def on_resize(window, w, h):
    global pov
    glViewport (0, 0, w, h)
    glMatrixMode (GL_PROJECTION)
    glLoadIdentity ()
    gluPerspective(60.0, w/h, 1.0, 20.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity ()
    gluLookAt (0.0, 0.0, 5.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)

def key_callback(window, key, scancode, action, mods):
    global angle, pov
    if action == glfw.PRESS:
        if key == glfw.KEY_UP:
            angle -= 5
        elif key == glfw.KEY_DOWN:
            angle += 5
        elif key == glfw.KEY_LEFT:
            pov = +10
        elif key == glfw.KEY_RIGHT:
            pov = -10

init()
#glfw.set_window_size_callback(window, on_resize)
glfw.set_key_callback(window, key_callback)
while not glfw.window_should_close(window):
    # Render here, e.g. using pyOpenGL
    on_draw()
    # Swap front and back buffers
    glfw.swap_buffers(window)

    # Poll for and process events
    glfw.poll_events()
    if vp_size_changed:
        vp_size_changed = False
        w, h = glfw.get_framebuffer_size(window)
        glViewport(0, 0, w, h)
glfw.terminate()
