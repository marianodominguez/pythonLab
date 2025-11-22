import random
import pygame

class Particle:
    def __init__(self, x, y, radius=10, color=(255, 255, 255)):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        
        # Random velocity
        self.vx = random.uniform(-2, 2)
        self.vy = random.uniform(-2, 2)
        
        self.mass = radius  # Simple mass approximation

    def move(self, gravity=0.5, friction=0.99, grav_center=(400, 300)):
        self.vx *= friction
        self.vy *= friction
        self.x += self.vx
        self.y += self.vy

        # Gravitational attraction to center
        dx = grav_center[0] - self.x
        dy = grav_center[1] - self.y
        dist = max(1, (dx**2 + dy**2)**0.5)
        force = 0.5 # Attraction strength
        self.vx += (dx / dist) * force
        self.vy += (dy / dist) * force

    def check_boundaries(self, width, height):
        # Bounce off left/right
        if self.x - self.radius < 0:
            self.x = self.radius
            self.vx *= -1
        elif self.x + self.radius > width:
            self.x = width - self.radius
            self.vx *= -1
            
        # Bounce off top/bottom
        if self.y - self.radius < 0:
            self.y = self.radius
            self.vy *= -1
        elif self.y + self.radius > height:
            self.y = height - self.radius
            self.vy *= -1

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), self.radius)
