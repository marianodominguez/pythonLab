# -*- coding: utf-8 -*-
import sys
import glfw

from OpenGL.GL import *
vp_size_changed = False

def display():
    glClear (GL_COLOR_BUFFER_BIT)
    glBegin(GL_POLYGON)
    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(20.0, 20.0, 1.5)
    glVertex3f(80.0, 20.0, -1.5)
    glVertex3f(80.0, 80.0, 0.0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(1.0, 0.0, 1.0)
    glVertex3f(120.0, 120.0, 0.0)
    glColor3f(1.0, 1.0, 0.0)
    glVertex3f(180.0, 120.0, 0.0)
    glColor3f(0.0, 1.0, 1.0)
    glVertex3f(180.0, 180.0, 0.0)
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(120.0, 180.0, 0.0)
    glEnd()   

    glFlush()

def resize(window, w,h):
    global vp_size_changed
    vp_size_changed = True

    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 200.0, 0.0, 200.0, -1.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def setup():
    glClearColor(1.0, 1.0, 1.0, 0.0)

if not glfw.init():
    print("Unable to get window")
    sys.exit(1)

glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 2)
glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 1)
# Use compatibility profile for immediate mode
# glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_COMPAT_PROFILE)
glfw.window_hint(glfw.OPENGL_DEBUG_CONTEXT, GL_TRUE)

window = glfw.create_window(640, 480, "Square", None, None)

if not window:
    glfw.terminate()
    sys.exit(1)

# Make the window's context current
glfw.make_context_current(window)
glfw.set_window_size_callback(window, resize)

#glewExperimental = GL_TRUE
#glewInit()
setup()
while not glfw.window_should_close(window):
    # Render here, e.g. using pyOpenGL
    display()
    # Swap front and back buffers
    glfw.swap_buffers(window)

    # Poll for and process events
    glfw.poll_events()
    if vp_size_changed:
        vp_size_changed = False
        w, h = glfw.get_framebuffer_size(window)
        glViewport(0, 0, w, h)
glfw.terminate()