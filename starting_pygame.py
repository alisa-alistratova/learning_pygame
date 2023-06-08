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
sky_surface = pygame.image.load('graphics/Sky.png').convert() #converst png image to something pygamne can work with.
ground_surface = pygame.image.load('graphics/ground.png').convert()
text_surface = test_font.render('My Game', False, 'Gray') #text, AA (rounds corners), color.

#RECTANGLES

snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha() # so iot looks nicer
#snail_x_position = 600
snail_rectangle = snail_surface.get_rect(midbottom = (80,300))

player_surface = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
#player_rectangle = pygame.Rect(left,top,width,height)
player_rectangle = player_surface.get_rect(midbottom = (80,300))

while True:

  #event loop
  for event in pygame.event.get():
      if event.type == pygame.QUIT:
          pygame.quit() #opposite of pygame.init
          exit()
      #if event.type == pygame.MOUSEMOTION:
      if event.type == pygame.MOUSEBUTTONDOWN:
        print('mouse down')
  #draw all our elements
  #update everything

  #screen.blit(test_surface,(300,300)) #blit - block image transfer
  #screen.blit(test_surface2,(0,0))
  
  screen.blit(sky_surface,(0,0))
  screen.blit(ground_surface,(0,300))
  screen.blit(text_surface, (300,50)) #x,y
  
  # snail_x_position += -10 #speed, fps. (+ direction)
  # if snail_x_position < -100:
  #   snail_x_position = 600
    
  #screen.blit(snail_surface, (snail_x_position, 265))
  snail_rectangle.x -= 4
  #snail_rectangle.left += -1
  if snail_rectangle.right <= 0: snail_rectangle.left = 800
  screen.blit(snail_surface, snail_rectangle)

  #player_rectangle.left += 3
  screen.blit(player_surface, player_rectangle)

  #COLLISION
  # if (player_rectangle.colliderect(snail_rectangle)):
  #   print('collision')

  #mouse_pos = pygame.mouse.get_pos()
  #if player_rectangle.collidepoint(mouse_pos): #gets the mouse position and prints collidison when mouse is there.
    #print(pygame.mouse.get_pressed())

  #rect1.collidepoint(xy,)

  pygame.display.update()
  clock.tick(60)

#Surfaces (Regular + Display Surface)
#Display surface - think of it like a poster to put things on (can have only 1)
#(Regular) surface - things to put on the display surface (can have as many as necessary)

#Plain Color Surface


#Text Surface
#1. creating font
#2. write text on surface


#Basic Animation

