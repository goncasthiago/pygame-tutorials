import pygame, sys, time
from settings import *
 
 
class Game:
    def __init__(self):
        
        # general setup
        pygame.init()
        self.display_surface = pygame.display.set_mode((WIDTH,HEIGHT))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption('Jogo do Arthur')
 
    def run(self):
        last_time = time.time()
        while True:
            
            # delta time
            dt = time.time() - last_time
            last_time = time.time()
 
            # event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
 
            # update window
            #self.display_surface.fill('green')
            pygame.display.update()
            #self.clock.tick(FPS)
 
if __name__ == '__main__':
    game = Game()
    game.run()