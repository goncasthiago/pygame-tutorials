import pygame
from sys import exit
from random import randint

def display_score():
    global counter_time
    counter_time = int(pygame.time.get_ticks()/1000) - start_time
    #if counter_time % 10 == 0: screen_time += 1
    score_surf = test_font.render( f"Score: {counter_time}" , False , (64,64,64) )
    score_rect = score_surf.get_rect(center = (WIDTH/2,50))
    screen.blit(score_surf, score_rect)
    return counter_time
    
    #print(screen_time)

def obstacle_movement(obstacle_list):

    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 5

            if obstacle_rect.bottom == 300: screen.blit(snail_surface, obstacle_rect)
            else: screen.blit(fly_surface, obstacle_rect)

        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]
        
        return obstacle_list
    else: return []

def collisions(player, obstacles):
    if obstacles:
        for obstacle_rect in obstacles:
            if player.colliderect(obstacle_rect): return False
    return True




pygame.init()

WIDTH = 800
HEIGHT = 400
SURF = 300
at_ground = True
game_active = False
start_time = 0
score = 0

#Score text
test_font = pygame.font.Font('font/Pixeltype.ttf',50)
#Create a score surface at beggining of the game
# score_surface = test_font.render('My game', False, (64,64,64))
# score_rect = score_surface.get_rect(center = (WIDTH/2,50))

#Start Screen
title_surf = test_font.render("Ruuuuuuner", False, (111,196,169))
title_rect = title_surf.get_rect(center = (WIDTH/2,50))

game_message = test_font.render('Press space to run', False, (111,196,169))
game_message_rect = game_message.get_rect(center = (WIDTH/2,HEIGHT-50))




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
fly_surface = pygame.image.load('graphics/Fly/Fly1.png').convert_alpha()
#obstacles
#snail_rect = snail_surface.get_rect(midbottom = (815,SURF))
#fly_rect = fly_surface.get_rect(midbottom = (815,SURF/2))
#snail_rect.left = 815

obstacle_rect_list = []

#player

player_surface = pygame.image.load('graphics\Player\player_walk_1.png').convert_alpha()
#player_rect = pygame.Rect(left,top,width,height)
player_rect = player_surface.get_rect( midbottom = (80,300))

#intro screen
player_stand = pygame.image.load('graphics/Player/player_stand.png').convert_alpha()
#player_stand = pygame.transform.scale(player_stand, (200,400))
#player_stand = pygame.transform.scale2x(player_stand)
player_stand = pygame.transform.rotozoom(player_stand,0,2)
player_stand_rect = player_stand.get_rect(center=(400,200))

#config
out_right = 815 #spawn on the right
out_left = -60  #spawn on the left
snail_velocity = 4.5
velocity = 1
player_gravity = 0

#Timer

obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1400)

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

                
        if event.type == obstacle_timer and game_active:
            if randint(0,2):
                obstacle_rect_list.append( snail_surface.get_rect(midbottom = (randint(900,1100),SURF)))

            else:
                obstacle_rect_list.append( fly_surface.get_rect(midbottom = (randint(900,1100),SURF/2)))
                    
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
        pygame.draw.lines(screen, 'Gold',True,((2,2),(2,HEIGHT-2),(WIDTH-2,HEIGHT-2),(WIDTH-2,2)),3)

        
        #score
        score = display_score()

        

        #Player

        player_rect.top += player_gravity
        
        if player_rect.bottom < 300:
            player_gravity += 1
            at_ground = False
        else:
            player_gravity = 0
            at_ground = True
            #back to ground
            player_rect.bottom = 300

        screen.blit( player_surface, player_rect)
        
        #obstacle movement
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)
        
        #collisions
        game_active = collisions(player_rect, obstacle_rect_list)


       
    else:
        screen.fill((94,129,162))  
        screen.blit(player_stand,player_stand_rect)
        obstacle_rect_list.clear()
        player_rect.midbottom = (80,300)
        player_gravity = 0
        if score != 0:
            score_message = test_font.render(f"Your Score: {score}",False, (111,196,169))
            score_message_rect = score_message.get_rect(center = (WIDTH/2,50))
            screen.blit(score_message,score_message_rect)
        else:
            screen.blit(title_surf, title_rect)
        screen.blit(game_message,game_message_rect)
        # screen.fill('Gold')


    pygame.display.update()
    clock.tick(60)