import pygame
import random
from circleshape import *
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.position = pygame.Vector2(x, y)

    def draw(self, screen):
        pygame.draw.circle(screen, "white",self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        self.angle = random.uniform(20, 50)
        self.new_radius = self.radius - ASTEROID_MIN_RADIUS
        a1d = self.velocity.rotate(self.angle) # How can you use self.velocity?
        a2d = self.velocity.rotate(-self.angle)  # Same idea!
        a1 = Asteroid(self.position.x, self.position.y, self.new_radius) # How do you spawn at the current position?
        a2 = Asteroid(self.position.x, self.position.y, self.new_radius)  # Same for the second!
        a1.velocity = a1d * 1.2  # Use a1d, not self.velocity!
        a2.velocity = a2d * 1.2 # Use a2d!