import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS
from constants import SCREEN_WIDTH
from constants import SCREEN_HEIGHT

class Shot(CircleShape):

    def __init__(self, x, y):

        super().__init__(x, y, SHOT_RADIUS)
        self.position = pygame.Vector2(x, y)

    def draw(self, screen):
        pygame.draw.circle(screen, "red", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
        if self.is_off_screen():
            self.kill()

    def is_off_screen(self):
        return (
            self.position.x < 0 or self.position.x > SCREEN_WIDTH or
            self.position.y < 0 or self.position.y > SCREEN_HEIGHT
        )
