import pygame
from sys import exit
from random import randint, choice



class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        #player_walk_1 = pygame.image.load('graphics\Player\player_walk_1.png').convert_alpha()
        #player_walk_2 = pygame.image.load('graphics\Player\player_walk_2.png').convert_alpha()

        player_walk_1 = pygame.image.load('graphics\Player\\andando1.png').convert_alpha()
        player_walk_2 = pygame.image.load('graphics\Player\\andando2.png').convert_alpha()
        self.player_walk = [player_walk_1,player_walk_2]
        self.player_index = 0
        self.player_jump =  pygame.image.load('graphics\Player\pulando1.png').convert_alpha()

        self.image =  self.player_walk[self.player_index] #pygame.image.load("graphics/Player/player_walk_1.png").convert_alpha()
        self.rect = self.image.get_rect(midbottom = (80,300))
        self.gravity = 0

        self.jump_sound = pygame.mixer.Sound('audio/jump.mp3')
    
    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 300:
            self.gravity = -20
            self.jump_sound.play()
            self.jump_sound.set_volume(0.5)

    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 300:
            self.rect.bottom = 300
    
    def animation(self):

        if self.rect.bottom < 300:
        # display the jump surface whn player is not on the floor
            self.image = self.player_jump
    
        else:
        # play walking animation if the player is on the floor
            self.player_index += 0.1
            if self.player_index > len(self.player_walk) : self.player_index = 0
            self.image = self.player_walk[int(self.player_index)]

    
    def update(self):
        self.player_input()
        self.apply_gravity()
        self.animation()

class Obstacle(pygame.sprite.Sprite):
    def __init__(self,type):
        super().__init__()
        if type == 'fly':
            fly_1 = pygame.image.load('graphics/Fly/foguete1.png').convert_alpha()
            fly_2 = pygame.image.load('graphics/Fly/foguete2.png').convert_alpha()
            self.frames = [fly_1, fly_2]
            y_pos = 150
            
        
        if type == 'snail':
            snail_1 = pygame.image.load('graphics/snail/tartametal1.png').convert_alpha()
            snail_2 = pygame.image.load('graphics/snail/tartametal2.png').convert_alpha()
            self.frames = [snail_1, snail_2]
            y_pos = 300
            

        self.index = 0
        self.image = self.frames[self.index]
        self.rect = self.image.get_rect(midbottom = (randint(900,1100),y_pos))
            
    def animation(self ):

        self.index += 0.1

        if self.index >= len(self.frames): self.index = 0
        self.image = self.frames[int(self.index)]
    
    def update(self):
        self.animation()
        self.rect.x -= 6
        self.destroy()

    def destroy(self):
        if self.rect.x <= -100:
            self.kill()
            

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

def collisions_sprite():
    if pygame.sprite.spritecollide(player.sprite,obstacle_group, False):
        obstacle_group.empty()
        return False
    else:
        return True

def player_animation():
    global player_surface, player_index
    
    if player_rect.bottom < 300:
        # display the jump surface whn player is not on the floor
        player_surface = player_jump
    
    else:
        # play walking animation if the player is on the floor
        player_index += 0.1
        if player_index > len(player_walk) : player_index = 0
        player_surface = player_walk[int(player_index)]



pygame.init()

WIDTH = 800
HEIGHT = 400
SURF = 300
at_ground = True
game_active = False
start_time = 0
score = 0
bg_Music = pygame.mixer.Sound('audio/music.wav')

#Score text
test_font = pygame.font.Font('font/Pixeltype.ttf',50)
#Create a score surface at beggining of the game
# score_surface = test_font.render('My game', False, (64,64,64))
# score_rect = score_surface.get_rect(center = (WIDTH/2,50))

#Start Screen
title_surf = test_font.render("Tutu Ruuuuuuner", False, (111,196,169))
title_rect = title_surf.get_rect(center = (WIDTH/2,50))

game_message = test_font.render('Press space to run', False, (111,196,169))
game_message_rect = game_message.get_rect(center = (WIDTH/2,HEIGHT-50))




#config
screen = pygame.display.set_mode((WIDTH,HEIGHT)) 
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()

player = pygame.sprite.GroupSingle()
player.add(Player())

obstacle_group = pygame.sprite.Group()


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
# snail_frame_1 = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
# snail_frame_2 = pygame.image.load('graphics/snail/snail2.png').convert_alpha()
# snail_frames = [snail_frame_1,snail_frame_2]
# snail_index = 0
# snail_surface = snail_frames[snail_index]
# #fly
# fly_frame_1 = pygame.image.load('graphics/Fly/Fly1.png').convert_alpha()
# fly_frame_2 = pygame.image.load('graphics/Fly/Fly2.png').convert_alpha()
# fly_frames = [fly_frame_1, fly_frame_2]
# fly_index = 0
# fly_surface = fly_frames[fly_index]

#obstacles
#snail_rect = snail_surface.get_rect(midbottom = (815,SURF))
#fly_rect = fly_surface.get_rect(midbottom = (815,SURF/2))
#snail_rect.left = 815

# obstacle_rect_list = []

#player

# player_walk_1 = pygame.image.load('graphics\Player\player_walk_1.png').convert_alpha()
# player_walk_2 = pygame.image.load('graphics\Player\player_walk_2.png').convert_alpha()
# player_walk = [player_walk_1,player_walk_2]
# player_index = 0
# player_jump =  pygame.image.load('graphics\Player\jump.png').convert_alpha()

##player_rect = pygame.Rect(left,top,width,height)
# player_surface = player_walk[player_index]
# player_rect = player_surface.get_rect( midbottom = (80,300))

#intro screen
# player_stand = pygame.image.load('graphics/Player/player_stand.png').convert_alpha()
# #player_stand = pygame.transform.scale(player_stand, (200,400))
# #player_stand = pygame.transform.scale2x(player_stand)
# player_stand = pygame.transform.rotozoom(player_stand,0,2)
# player_stand_rect = player_stand.get_rect(center=(400,200))

#Face
face_frame_1 = pygame.image.load('graphics/Player/cara1.png').convert_alpha()
face_frame_2 = pygame.image.load('graphics/Player/cara2.png').convert_alpha()
#face_frame_1 = pygame.transform.rotozoom(face_frame_1,0,2)
#face_frame_2 = pygame.transform.rotozoom(face_frame_2,0,2)
face_frames = [face_frame_1, face_frame_2]
face_index = 0
face_surface = face_frames[face_index]
face_rect = face_surface.get_rect(center=(400,200))



#config
out_right = 815 #spawn on the right
out_left = -60  #spawn on the left
snail_velocity = 4.5
velocity = 1
player_gravity = 0

#Timer

obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1400)

snail_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(snail_animation_timer, 500)

fly_animation_timer = pygame.USEREVENT + 3
pygame.time.set_timer(fly_animation_timer, 200)

face_animation_timer = pygame.USEREVENT + 4
pygame.time.set_timer(face_animation_timer, 1200)

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

             
                        
            
            
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE :
                start_time = int(pygame.time.get_ticks()/1000)
                #screen_time = 0
                game_active = True
                bg_Music.play(loops = -1)

        if game_active:        
            if event.type == obstacle_timer:
                obstacle_group.add(Obstacle(choice(['fly', 'snail', 'snail', 'snail', 'snail'])))
                
                #if randint(0,2):
                #    obstacle_rect_list.append( snail_surface.get_rect(midbottom = (randint(900,1100),SURF)))
                #else:
                #    obstacle_rect_list.append( fly_surface.get_rect(midbottom = (randint(900,1100),SURF/2)))
                    
            # if event.type == snail_animation_timer:
            #     if snail_index == 0: snail_index = 1
            #     else: snail_index = 0
            #     snail_surface = snail_frames[snail_index]
            
            # if event.type == fly_animation_timer:
            #     if fly_index == 0: fly_index = 1
            #     else: fly_index = 0
            #     fly_surface = fly_frames[fly_index]

                    
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

        # player_rect.top += player_gravity
        
        # if player_rect.bottom < 300:
        #     player_gravity += 1
        #     at_ground = False
        # else:
        #     player_gravity = 0
        #     at_ground = True
        #     #back to ground
        #     player_rect.bottom = 300
        # player_animation()
        # screen.blit( player_surface, player_rect)
        
        player.draw(screen)
        player.update()

        obstacle_group.draw(screen)
        obstacle_group.update()

        #obstacle movement
        # obstacle_rect_list = obstacle_movement(obstacle_rect_list)
        
        #collisions
        # game_active = collisions(player_rect, obstacle_rect_list)
        game_active = collisions_sprite()


       
    else:
        if event.type == face_animation_timer:
            if face_index == 0: face_index = 1
            else: face_index = 0
            face_surface = face_frames[face_index]
 
        screen.fill((94,129,162))  
        #screen.blit(player_stand,player_stand_rect)
        screen.blit(face_surface,face_rect)
        bg_Music.stop()
        # obstacle_rect_list.clear()
        # player_rect.midbottom = (80,300)
        # player_gravity = 0
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