import pygame

class Game:
    def __init__(self, screen):
        self.running = True
        self.screen = screen
    def handle_events(self):
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                self.running = False
    def tick(self):
        pass
    def draw(self):
	    pygame.display.update() 

pygame.init() 

#Create screen surface 
screen = pygame.display.set_mode((480, 360)) 
pygame.display.set_caption("Collision... Probably?") 

game = Game(screen)
while game.running: 
    game.handle_events()
    game.tick()
    game.draw()