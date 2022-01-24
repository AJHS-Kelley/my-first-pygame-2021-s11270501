#Simple Animation with Pygame, Ryan Kelley, 12/08/21,10:13AM, v0.0

import pygame, sys,time
from pygame.locals import *


pygame.init()


WINDOWWIDTH = 400
WINDOWHEIGHT = 400
windowSurface = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT),0,32)
pygame.display.set_caption('Animation Example!')



DOWNLEFT = 'downleft'
DOWNRIGHT='downright'
UPLEFT = 'upleft'
UPRIGHT = 'upright'

MOVESPEED = 4

WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)



b1 = {'rect':pygame.Rect(300,80,50,100),'color':RED, 'dir' :UPRIGHT}
b2 = {'rect':pygame.Rect(200,200,20,20),'color':GREEN, 'dir' :UPLEFT}
b3 = {'rect':pygame.Rect(100,150,60,60),'color':BLUE, 'dir' :DOWNLEFT}
boxes = [b1,b2,b3] 


while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit() 