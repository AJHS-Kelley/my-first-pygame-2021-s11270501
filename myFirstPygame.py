# My First Pygame,Ryan Kelley,11/30/21, 12:17PM,v0.2

 import pygame , sys  
 from pygame.locals import *

 # Initialize Pygame 
 pygame.init()

#Setup the window to draw on
WindowSurface = pygame.display.set_mode((500,400),0,32)
pygame.display.set_caption('My first Pygame')

# Setup color values,
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
PURPLE = (255,0,255)
YELLOW = (249,215,28)