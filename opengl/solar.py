import OpenGL 
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys

year = 0
day = 0

def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glShadeModel(GL_FLAT)

def on_draw():
   glClear (GL_COLOR_BUFFER_BIT)
   glColor3f (1.0, 1.0, 1.0)

   glPushMatrix()
   glutWireSphere(1.0, 20, 16)   # draw sun */
   glRotatef (year, 0.0, 1.0, 0.0)
   glTranslatef (2.0, 0.0, 0.0)
   glRotatef (day, 0.0, 1.0, 0.0)
   glutWireSphere(0.2, 10, 8)    # draw smaller planet */
   glPopMatrix()
   glutSwapBuffers()

def on_resize(w, h):
   glViewport (0, 0, w, h)
   glMatrixMode (GL_PROJECTION)
   glLoadIdentity ()
   gluPerspective(60.0, w/h, 1.0, 20.0)
   glMatrixMode(GL_MODELVIEW)
   glLoadIdentity()
   gluLookAt (0.0, 0.0, 5.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)

def on_key_press(key, x, y):
    global day, year
    if key=='d':
       day = (day + 10) % 360
       glutPostRedisplay()
    if key=='D':
       day = (day - 10) % 360
       glutPostRedisplay()
    if key=='y':
       year = (year + 5) % 360
       glutPostRedisplay()
    if key=='Y':
       year = (year - 5) % 360
       glutPostRedisplay()

glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(500, 500)
glutInitWindowPosition(100, 100)
glutCreateWindow("solar")
init()
glutDisplayFunc(on_draw)
glutReshapeFunc(on_resize)
glutKeyboardFunc(on_key_press)
glutMainLoop()
