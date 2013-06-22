from pyglet.gl import *
import pyglet.window
from pyglet.window import key


class BaseWindow(pyglet.window.Window):

    usage_info = 'Use the arrow keys to rotate the image'

    nrange = 100.0

    def __init__(self, width=500, height=500, caption=None, resizable=True,
                 **kwargs):
        super(BaseWindow, self).__init__(width = width,
                                         height = height,
                                         caption = caption,
                                         resizable = resizable,
                                         **kwargs)

        self.xrot = 0.0
        self.yrot = 0.0

    def on_resize(self, width, height):
        # Prevent divide by zero
        height = (height if (height > 0) else 1)

        # Set viewport to window dimensions
        glViewport(0, 0, width, height)

        # Reset projection matrix stack
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()

        # Establish clipping volume (left, right, bottom, top, near, far)
        ratio = float(width) / float(height)
        if ratio <= 1.0:
            xrange = self.nrange
            yrange = self.nrange / ratio
        else:
            xrange = self.nrange * ratio
            yrange = self.nrange
        glOrtho(-xrange, xrange, -yrange, yrange, -self.nrange, self.nrange)

        # Reset model view matrix stack
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

    def on_key_press(self, symbol, modifiers):
        if symbol == key.UP:
            self.xrot -= 5.0
        elif symbol == key.DOWN:
            self.xrot += 5.0
        elif symbol == key.LEFT:
            self.yrot -= 5.0
        elif symbol == key.RIGHT:
            self.yrot += 5.0

        if self.xrot > 356.0:
            self.xrot = 0.0
        elif self.xrot < -1.0:
            self.xrot = 355.0

        if self.yrot > 356.0:
            self.yrot = 0.0
        elif self.yrot < -1.0:
            self.yrot = 355.0

    def setup(self):
        # Black background
        glClearColor(0.0, 0.0, 0.0, 1.0)

        # Set drawing color to green
        glColor3f(0.0, 1.0, 0.0)

    def predraw(self):
        glPushMatrix()
        glRotatef(self.xrot, 1.0, 0.0, 0.0)
        glRotatef(self.yrot, 0.0, 1.0, 0.0)

    def draw(self):
        raise NotImplementedError

    def postdraw(self):
        glPopMatrix()

    def run(self):
        print self.usage_info
        self.setup()
        while not self.has_exit:
            self.dispatch_events()
            self.clear()
            self.predraw()
            self.draw()
            self.postdraw()
            self.flip()            