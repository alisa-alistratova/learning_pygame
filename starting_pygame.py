import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400)) #width = 800, height = 400
pygame.display.set_caption('Whatever')
clock = pygame.time.Clock() #controls time & framerate
test_font = pygame.font.Font('font/Pixeltype.ttf', 50) #type,size
'''
#PLAIN COLOR SURFACE
test_surface = pygame.Surface((200,100))
test_surface.fill((195,255,236))
#test_surface2 = pygame.Surface((600,100))
#test_surface2.fill((255,255,195))
'''
#IMAGE SURFACE
sky_surface = pygame.image.load('graphics/Sky.png')
ground_surface = pygame.image.load('graphics/ground.png')
text_surface = test_font.render('My Game', False, 'Gray') #text, AA (rounds corners), color.

while True:
    #event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() #opposite of pygame.init
            exit()
    #draw all our elements
    #update everything

    #screen.blit(test_surface,(300,300)) #blit - block image transfer
    #screen.blit(test_surface2,(0,0))
    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,300))
    screen.blit(text_surface, (300,50)) #x,y
    pygame.display.update()
    clock.tick(60)

#Surfaces (Regular + Display Surface)
#Display surface - think of it like a poster to put things on (can have only 1)
#(Regular) surface - things to put on the display surface (can have as many as necessary)

#Plain Color Surface


#Text Surface
#1. creating font
#2. write text on surface


