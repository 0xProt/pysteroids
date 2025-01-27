import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
            return
        else:
            split_angle = random.uniform(20, 50)
            split1 = self.velocity.rotate(split_angle)
            split2 = self.velocity.rotate(-split_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            child1 = Asteroid(self.position[0], self.position[1], new_radius)
            child2 = Asteroid(self.position[0], self.position[1], new_radius)
            child1.velocity = split1 * 1.2
            child2.velocity = split2 * 1.2
            self.kill()
