import pygame
from constants import *
from player import Player


def main():
    pygame.init()
    x = SCREEN_WIDTH/2
    y = SCREEN_HEIGHT/2
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers  = (updatable, drawable)
    player = Player(x, y)

    while(1):
        screen.fill((0, 0, 0))
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                return
            for thing in updatable:
                thing.update(dt)
            for thing in drawable:
                thing.draw(screen)
            
            dt = clock.tick(60)/1000
            pygame.display.flip()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()