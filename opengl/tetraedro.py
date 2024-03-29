import OpenGL 
import math
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import pygame
import sys
from pygame.locals import *

SCREEN_SIZE  = width,height = 800,600

angle=0
pov = 0.0
h = math.sqrt(3)/2

# Define a simple function to create ctypes arrays of floats:
def vec(*args):
    return (GLfloat * len(args))(*args)

def init():
    
    lightpos = vec(20, 20, 1, 0)
    red = vec(0.8, 0.1, 0.0, 1.0)

    green = vec(0.0, 0.8, 0.2, 1.0)
    blue = vec(0.2, 0.2, 1.0, 1.0)
    
    glShadeModel(GL_FLAT)
    glClearColor(0.0, 0.0, 0.0, 0.0)

    glEnable(GL_COLOR_MATERIAL)
    
    glMatrixMode(GL_MODELVIEW)
    gluOrtho2D(0, width, height, 0)
    glLoadIdentity()

    glEnable(GL_DEPTH_TEST)    

    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)        
    glLight(GL_LIGHT0, GL_POSITION,  lightpos)    

def triangleFace():
    glBegin(GL_TRIANGLES)
    glVertex3f(-0.5, h, 1.0)    
    glVertex3f(0.5, h, 1.0)
    glVertex3f(0.0, 0.0, 1.0)
    
    glEnd()

def draw():
    print(angle,pov)

    glClear(GL_COLOR_BUFFER_BIT)
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
    pygame.display.flip()

def run():
    global angle, pov
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE, OPENGL|DOUBLEBUF)
    
    init()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            if event.type == KEYDOWN:    
                if event.key == pygame.K_UP:
                    angle -= 5.0
                if event.key == pygame.K_DOWN:
                    angle += 5.0
                if event.key == pygame.K_LEFT:
                    pov +=1
                if event.key == pygame.K_RIGHT:
                    pov -=1
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
                # Show the screen
                draw()
run()
