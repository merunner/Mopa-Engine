#!/usr/bin/env python

import pygame
from pygame.locals import *
import sys
import random

class MopaGame(object):

    

    def __init__(self):
        self.DISP_MODE = (800,600)
        pygame.display.init()    
        self.screen = pygame.display.set_mode(self.DISP_MODE, FULLSCREEN, 32)    
      
    def load(self):
        self.game.load()
    
    def listen(self):
        pass
        
    def update(self):
        print 'Update!'
        
    def render(self):
        print 'Render!'
        
    def flush(self):
        print 'Flush!'

    def initStars(self):
        qtdStars = 100
        stars = []        
        radius = 1
        for _ in range(qtdStars):
            surface = pygame.Surface((radius,radius))
            y = random.randint(10, self.DISP_MODE[1])
            x = random.randint(10, self.DISP_MODE[0])
            pygame.draw.circle(surface, (255, 255,255), (0,0), radius)
            
            stars.append((surface,x,y))
            
        return stars
    

    def run(self):
        
        #random.seed(3)
        stars = self.initStars()
        
        
        
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    sys.exit()
                if event.type == KEYDOWN and event.key == K_ESCAPE:
                    sys.exit()

            self.screen.fill((0,0,0))
            for star in stars:
                self.screen.blit(star[0], (star[1],star[2]))
            
            pygame.display.update()


if __name__ == '__main__':
    mopaEngine = MopaGame()
    mopaEngine.run()
