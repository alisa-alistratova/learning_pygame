import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400)) #width = 800, height = 400
pygame.display.set_caption('Whatever')
clock = pygame.time.Clock() #controls time & framerate

while True:
    #event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() #opposite of pygame.init
            exit()
    #draw all our elements
    #update everything
    pygame.display.update()
    clock.tick(60)

#Surfaces (Regular + Display Surface)
#Display surface - think of it like a poster to put things on (can have only 1)
#(Regular) surface - things to put on the display surface (can have as many as necessary)

#Plain Color Surface
