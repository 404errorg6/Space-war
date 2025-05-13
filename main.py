import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import *
from shot import Shot


def main():
    pygame.init()
    x = SCREEN_WIDTH/2
    y = SCREEN_HEIGHT/2
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers  = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (updatable, drawable, shots)
    AF = AsteroidField()
    player = Player(x, y)



    while(1):
        screen.fill((0, 0, 0))
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)
        for objects in asteroids:
            if objects.collide(player):
                sys.exit("Game over!")
        for asteroid in asteroids:
            for bullet in shots:
                if bullet.collide(asteroid):
                    bullet.kill()
                    asteroid.split()

        for thing in drawable:
            thing.draw(screen)
            
            
        pygame.display.flip()
        dt = clock.tick(60)/1000
            
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()