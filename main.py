import pygame
import sys

from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init
    pygame.font.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    black = (0, 0, 0)
    white = (255, 255, 255)
    score = 0
    lives = 5
    is_alive = True

    clock = pygame.time.Clock()

    font = pygame.font.Font(None, 36)

    player_x = SCREEN_WIDTH / 2
    player_y = SCREEN_HEIGHT / 2

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = updateable
    Shot.containers = (shots, updateable, drawable)

    player = Player(player_x, player_y, PLAYER_SIZE)

    asteroid_field = AsteroidField()


    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for sprites in updateable:
            sprites.update(dt)

        for asteroid in asteroids:
            if player.check_collision(asteroid) == True and is_alive == True:
                    lives -= 1
                    player.kill()
                    clear_asteroids(asteroids)
                    break

        for asteroid in asteroids:
            for shot in shots:
                if shot.check_collision(asteroid) == True:
                    score += 50
                    shot.kill()
                    asteroid.kill()
                    asteroid.split()

        if not player.is_alive and lives > 0:
            player.respawn()

        if lives < 1:
            sys.exit()

        screen.fill(black)

        score_text = font.render(f"Score: {score}", True, white)
        lives_text = font.render(f"Lives: {lives}", True, white)

        screen.blit(score_text, (10, 10))
        screen.blit(lives_text, (SCREEN_WIDTH - 100, 10))

        for sprites in drawable:
            sprites.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000

        def clear_asteroids(asteroids):
            for asteroid in list(asteroids):
                asteroid.kill()

if __name__ == "__main__":
    main()
