#Simple Animation with Pygame, Ryan Kelley, 12/08/21,10:13AM, v0.0

import pygame, sys,time
from pygame.locals import *


pygame.init()

WINDOWWIDTH = 400
WINDOWHEIGHT = 400
windowSurface = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT),0,32)
pygame.display.set_caption('Animation Example!')