import pygame
import time
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import *
from shot import Shot
from score import Score



def main():
    pygame.init()
    score = 0
    x = SCREEN_WIDTH/2
    y = SCREEN_HEIGHT/2
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    HIGH_SCORE = 0

    Player.containers  = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (updatable, drawable, shots)
    Score.containers = (updatable, drawable)
    
   
    AF = AsteroidField()
    player = Player(x, y)



    while(1):
        screen.fill((0, 0, 0))
        s = Score(score)
        s.score()
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)
        for objects in asteroids:
            flag = 0
            if objects.collide(player):
                #if score > HIGH_SCORE:
                #    HIGH_SCORE = score
                #if s.high():
                #    flag = 1
                    
                #else:
                    sys.exit("Game over!")
            #if flag:
            #    break
        for asteroid in asteroids:
            for bullet in shots:
                if bullet.collide(asteroid):
                    bullet.kill()
                    asteroid.split()
                    score += 10

        for thing in drawable:
            thing.draw(screen)
            
            
        pygame.display.flip()
        dt = clock.tick(60)/1000
            
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()