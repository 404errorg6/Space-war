import pygame

from constants import *



class Score:
    def __init__(self, score):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        font1 = pygame.font.Font("freesansbold.ttf", 25)

        self.text1 = font1.render(f"Score: {score}", True, "white")
    #    self.text2 = font1.render(f"Highscore: {HIGH_SCORE}", True, "yellow")
    #    self.text3 = font1.render(f"Press Y to play again and N to quit.", True, "white")

    #def input(self):
    #    while True:
    #        for event in pygame.event.get():
    #            key = pygame.key.get_pressed()
    #            if key[pygame.K_y]:
    #                return True
    #            if key[pygame.K_n]:
    #                return False

    def score(self):
        self.screen.blit(self.text1, (SCREEN_WIDTH//1.2, SCREEN_HEIGHT//1.05))
    
    #def high(self):
        
        #self.screen.blit(self.text2, (SCREEN_WIDTH/2, SCREEN_HEIGHT/5))
        #self.screen.blit(self.text3, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
        #pygame.display.update()
        #return self.input()