#!/usr/bin/env python

import math

import pyglet.clock
from pyglet.gl import *
import pyglet.window


class Window(pyglet.window.Window):

    def __init__(self):
        super(Window, self).__init__(caption = 'OpenGL Single Buffered',
                                     config = Config(double_buffer=False))

        self.radius = 0.1
        self.angle = 0.0

        glClearColor(0.0, 0.0, 1.0, 1.0)

        pyglet.clock.schedule_interval(self.update, 0.05)

    def on_resize(self, width, height):
        glViewport(0, 0, width, height)

        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()

        gluOrtho2D(-4.0, 4.0, -3.0, 3.0)

        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

    def update(self, dt):
        if self.angle == 0.0:
            glClear(GL_COLOR_BUFFER_BIT)

        glBegin(GL_POINTS)
        glVertex2d(self.radius * math.cos(self.angle),
                   self.radius * math.sin(self.angle))
        glEnd()

        self.radius *= 1.01
        self.angle += 0.1

        if self.angle > 30.0:
            self.radius = 0.1
            self.angle = 0.0

        glFlush()

    def run(self):
        while not self.has_exit:
            self.dispatch_events()
            pyglet.clock.tick()


if __name__ == '__main__':
    Window().run()