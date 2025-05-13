import random
from circleshape import *
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "red", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            angle = random.uniform(20, 50)
            v1 = self.velocity.rotate(angle)
            v2 = self.velocity.rotate(-angle)
            new_rad = self.radius - ASTEROID_MIN_RADIUS
            A1 = Asteroid(self.position.x, self.position.y, new_rad)
            A2 = Asteroid(self.position.x, self.position.y, new_rad)
            A1.velocity = v1 * 1.2
            A2.velocity = v2 * 1.2
