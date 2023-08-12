import pygame
from sys import exit

pygame.init()

WIDTH = 800
HEIGHT = 400

screen = pygame.display.set_mode((WIDTH,HEIGHT)) 
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf',50)
text_surface = test_font.render('My game', False, 'Black')
score_rect = text_surface.get_rect(center = (WIDTH/2,HEIGHT/2))

#brackgroud surfaces
#test_surface.fill('green')
##Sky
sky_surface = pygame.Surface((800,400))
sky_surface = pygame.image.load('graphics/Cielo.png').convert()
##Ground
ground_surface = pygame.Surface((800,100))
ground_surface = pygame.image.load('graphics/ground.png').convert()

#Actors
#snail
snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()

snail_rect = snail_surface.get_rect(midbottom = (815,300))
snail_rect.left = 815
#player
player_surface = pygame.image.load('graphics\Player\player_walk_1.png').convert_alpha()
#player_rect = pygame.Rect(left,top,width,height)
player_rect = player_surface.get_rect(midbottom = (50,300))

out_right = 815
out_left = -60
velocity = 1
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        #collision with event loop
        #if event.type == pygame.MOUSEMOTION:
        #    print(player_rect.collidepoint(event.pos))
        
        #show mouse (x,y)
        #if event.type == pygame.MOUSEMOTION:
        #    print(event.pos)
        #Mouse "click"
        #if event.type == pygame.MOUSEBUTTONDOWN:
        #    print(event.pos)

    #draw all our elements
    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,300))
    screen.blit(text_surface,score_rect)

    #snail moviment
    snail_rect.x -= velocity
    if snail_rect.x < out_left: snail_rect.x = out_right
    screen.blit(snail_surface,snail_rect)
    #Player
    screen.blit( player_surface, player_rect)
    player_rect.left += 1
    if player_rect.x > out_right: player_rect.x = out_left

    #collisions
    #if player_rect.colliderect(snail_rect):
    #    print("Collision")

    #mouse
    #mouse_pos = pygame.mouse.get_pos()
    #if player_rect.collidepoint(mouse_pos):
    #    #print('collision')
    #    print(pygame.mouse.get_pressed())

    #update everything

    pygame.display.update()
    clock.tick(60)