import unittest
from particle import Particle

class TestParticle(unittest.TestCase):
    def test_movement(self):
        p = Particle(100, 100)
        p.vx = 5
        p.vy = -5
        p.move()
        self.assertEqual(p.x, 105)
        self.assertEqual(p.y, 95)

    def test_boundary_bounce_right(self):
        width = 200
        height = 200
        p = Particle(195, 100, radius=10)
        p.vx = 10
        p.move() # x becomes 205
        p.check_boundaries(width, height)
        self.assertEqual(p.x, 190) # Should be capped at width-radius (190)? No, logic sets it to width-radius.
        # Wait, my logic was:
        # if self.x + self.radius > width:
        #     self.x = width - self.radius
        #     self.vx *= -1
        
        # So if x was 205, radius 10. 205+10 = 215 > 200.
        # x becomes 200 - 10 = 190.
        # vx becomes -10.
        
        self.assertEqual(p.x, 190)
        self.assertEqual(p.vx, -10)

if __name__ == '__main__':
    unittest.main()
