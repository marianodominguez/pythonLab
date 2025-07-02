# -*- coding: utf-8 -*-
import sys
from OpenGL.GLUT import *
from OpenGL.GL import *

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

def resize(w,h):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 200.0, 0.0, 200.0, -1.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def setup():
    glClearColor(1.0, 1.0, 1.0, 0.0)

glutInit(sys.argv)
glutInitContextVersion(4,3)
glutInitContextProfile(GLUT_COMPATIBILITY_PROFILE)

glutInitDisplayMode(GLUT_SINGLE|GLUT_RGBA)
glutInitWindowSize(400,400)
glutCreateWindow("oldgl")
glutDisplayFunc(display)
glutReshapeFunc(resize)

#glewExperimental = GL_TRUE
#glewInit()
setup()
glutMainLoop()