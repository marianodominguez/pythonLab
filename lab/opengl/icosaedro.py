import OpenGL
import math
from OpenGL.GL import *
from pyglet.gl import *
from pyglet.window import key

# Direct OpenGL commands to this window.
window = pyglet.window.Window(resizable=True)
angle=20
pov = 0.0
h = math.sqrt(3)/2

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
    glVertex3f(0.5, h, 0)
    glVertex3f(-0.5, h, 0)

    glEnd()

@window.event
def on_draw():
    global angle,h,pov

    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 0.0, 1.0)

    glRotatef (pov, 0.0, 1.0, 1.0)
    pov=0
    glPushMatrix()

    triangleFace()
    #glTranslatef (2.0, 0.0, 0.0)

    glRotatef (60, 0.0, 0.0, 1.0)
    glRotatef (-angle, 0.5, h, 0.0)

    triangleFace()

    glPopMatrix()
    glPushMatrix()

    glRotatef (-60, 0.0, 0.0, 1.0)
    glRotatef (angle, -0.5, h, 0.0)

    triangleFace()
    glPopMatrix()
    glPushMatrix()

    glTranslatef (0.5, h, 0.0)
    glRotatef (60, 0.0, 0.0, 1.0)
    glRotatef (angle, -0.5, h, 0.0)

    triangleFace()

    glPopMatrix()

@window.event
def on_resize(w, h):
    global pov
    glViewport (0, 0, w, h)
    glMatrixMode (GL_PROJECTION)
    glLoadIdentity ()
    gluPerspective(60.0, w/h, 1.0, 20.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity ()
    gluLookAt (0.0, 0.0, 5.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
    return pyglet.event.EVENT_HANDLED

@window.event
def on_key_press(symbol, modifiers):
    global angle, pov
    if symbol == key.UP:
        angle -= 5
    elif symbol == key.DOWN:
        angle += 5
    elif symbol == key.LEFT:
        pov = +10
    elif symbol == key.RIGHT:
        pov = -10
    return pyglet.event.EVENT_HANDLED

init()
pyglet.app.run()
