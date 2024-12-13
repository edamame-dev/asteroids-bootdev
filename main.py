import pygame

from constants import *
from player import Player

def main():
    pygame.init
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    black = (0, 0, 0)
    clock = pygame.time.Clock()
    dt = 0
    player_x = SCREEN_WIDTH / 2
    player_y = SCREEN_HEIGHT / 2

    player = Player(player_x, player_y)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill(black)
        player.draw(screen)
        pygame.display.flip()


        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
