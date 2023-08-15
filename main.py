import pygame
from sys import exit

def display_score():
    global screen_time
    counter_time = int(pygame.time.get_ticks()/1000) - start_time
    #if counter_time % 10 == 0: screen_time += 1
    score_surf = test_font.render( f"Score: {counter_time}" , False , (64,64,64) )
    score_rect = score_surf.get_rect(center = (WIDTH/2,50))
    screen.blit(score_surf, score_rect)
    #print(screen_time)

pygame.init()

WIDTH = 800
HEIGHT = 400
SURF = 300
at_ground = True
game_active = True
start_time = 0
#screen_time = 0

#Score text
test_font = pygame.font.Font('font/Pixeltype.ttf',50)
#Create a score surface at beggining of the game
# score_surface = test_font.render('My game', False, (64,64,64))
# score_rect = score_surface.get_rect(center = (WIDTH/2,50))

#config
screen = pygame.display.set_mode((WIDTH,HEIGHT)) 
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()



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

snail_rect = snail_surface.get_rect(midbottom = (815,SURF))
snail_rect.left = 815
#player
player_surface = pygame.image.load('graphics\Player\player_walk_1.png').convert_alpha()
#player_rect = pygame.Rect(left,top,width,height)
player_rect = player_surface.get_rect( midbottom = (80,300))

out_right = 815
out_left = -60
snail_velocity = 4.5
velocity = 1
player_gravity = 0

while True:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:
            if event.type == pygame.KEYDOWN and at_ground :
                #print('key down')
                match event.key:
                    case pygame.K_SPACE:
                        #print("Space")
                        player_gravity = -20
                        
            
            if event.type == pygame.MOUSEBUTTONDOWN and at_ground:
                if player_rect.collidepoint(event.pos): 
                    player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE :
                start_time = int(pygame.time.get_ticks()/1000)
                #screen_time = 0
                game_active = True

                



        
        #if event.type == pygame.KEYUP:
        #    print('key up')
        
        #collision with event loop
        #if event.type == pygame.MOUSEMOTION:
        #    print(player_rect.collidepoint(event.pos))
        
        #show mouse (x,y)
        #if event.type == pygame.MOUSEMOTION:
        #    print(event.pos)
        #Mouse "click"
        #if event.type == pygame.MOUSEBUTTONDOWN:
        #    print(event.pos)
    if game_active:
        #draw all our elements
        screen.blit(sky_surface,(0,0))
        screen.blit(ground_surface,(0,300))
        display_score()
        #pygame.draw.rect(screen, 'Pink', score_rect)
        
        #score
        #pygame.draw.rect(screen, '#c0e8ec' , pygame.Rect.scale_by(score_rect, 1.3, 1.2),0,12)
        #screen.blit(score_surface,score_rect)
        

        #Main screen
        pygame.draw.lines(screen, 'Gold',True,((2,2),(2,HEIGHT-2),(WIDTH-2,HEIGHT-2),(WIDTH-2,2)),3)
        #snail moviment
        snail_rect.x -= snail_velocity
        if snail_rect.x < out_left: snail_rect.x = out_right
        screen.blit(snail_surface,snail_rect)


        #Player

        screen.blit( player_surface, player_rect)
        #player_rect.left += 1
        #if player_rect.x > out_right: player_rect.x = out_left
        player_rect.top += player_gravity
        
        if player_rect.bottom < 300:
            player_gravity += 1
            at_ground = False
        else:
            player_gravity = 0
            at_ground = True
            #back to ground
            player_rect.bottom = 300
        
        

        

        #collisions

        if snail_rect.colliderect(player_rect):
            #pygame.quit()
            #exit()
            at_ground = True
            player_rect.bottom = 300
            snail_rect.x = out_right
            game_active = False
            screen.fill('Gold')

        #if player_rect.colliderect(snail_rect):
        #    print("Collision")



        #mouse
        #mouse_pos = pygame.mouse.get_pos()
        #if player_rect.collidepoint(mouse_pos):
        #    #print('collision')
        #    print(pygame.mouse.get_pressed())

        #update everything

        #reading 
        # keys = pygame.key.get_pressed()
        # if keys[pygame.K_SPACE]:
        #     print("Jump")

        
    #else:
    #    screen.fill('Gold')

    pygame.display.update()
    clock.tick(60)