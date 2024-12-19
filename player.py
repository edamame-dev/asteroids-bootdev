import pygame
from triangleshape import TriangleShape
from circleshape import CircleShape
from constants import *
from shot import Shot

class Player(TriangleShape):
    def __init__(self, x, y, size):
        super().__init__(x, y, PLAYER_SIZE)
        self.position = pygame.Vector2(x, y)
        self.rotation = 0
        self.shot_timer = 0
        self.is_alive = True


    def draw(self, screen):
        pygame.draw.polygon(screen, "White", self.calculate_vertices(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        self.shot_timer -= dt
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        if self.shot_timer > 0:
            return
        self.shot_timer = PLAYER_SHOOT_COOLDOWN
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED

    def initial_position(self):
        return pygame.Vector2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    def respawn(self):
        self.position = self.initial_position()
        self.is_alive = True

    def kill(self):
        self.is_alive = False
