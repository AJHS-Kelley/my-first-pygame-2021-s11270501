# My First Pygame,Ryan Kelley,11/30/21, 12:17PM,v0.2

import pygame , sys
from pygame import pixelarray  
from pygame.locals import *

# Initialize Pygame 
pygame.init()

#Setup the window to draw on
windowSurface = pygame.display.set_mode((500,400),0,32)
pygame.display.set_caption('My first Pygame')

# Setup color values,
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
PURPLE = (255,0,255)
YELLOW = (249,215,28)

# Setup the fonts.
basicFont = pygame.font.SysFont(None,48)

text = basicFont.render('Hello, world!',True,WHITE, BLUE )
textRect = text.get_rect()
textRect.centerx = windowSurface.get_rect().centerx
textRect.centery = windowSurface.get_rect().centery


windowSurface.fill(YELLOW)


pygame.draw.polygon(windowSurface,GREEN,((146,0),(291,106),(236,277), (56,277),(0,106)))

pygame.draw.line(windowSurface,RED, (60,60), (120,60),4)
pygame.draw.line(windowSurface,WHITE, (75,60), (60,75),2)
pygame.draw.line(windowSurface,RED, (0,150), (150,0),1)



pygame.draw.circle(windowSurface,BLACK, (300,50),20,0)


pygame.draw.ellipse(windowSurface,PURPLE, (300,250,40,80),1)


pygame.draw.rect(windowSurface,PURPLE, (textRect.left-20,textRect.top-20,textRect.width+40,textRect.height+40))


pixArray=pygame.PixelArray(windowSurface)
pixArray[480][380]=BLUE
del pixArray

windowSurface.blit(text,textRect)


pygame.display.update()


while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.quit()
