import pygame

class Game:
    def __init__(self, screen):
        self.running = True

        self.screen = screen
        self.objects = (
            Player(),
            Tile([100, 0])
        )
    def handle_events(self):
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                self.running = False
    def tick(self):
        clock = pygame.time.Clock()
        dt = clock.tick(60)

        for obj in self.objects: obj.tick(60)
    def draw(self):
        self.screen.fill((0, 0, 0))
        for obj in self.objects: obj.draw()
        pygame.display.update()

class Player:
    def __init__(self, position = [0, 0]):
        self.position = position
        self.rect = pygame.Rect(position, (16, 16))
    def tick(self, dt):
        keys = pygame.key.get_pressed()
        keys_input = [
            keys[pygame.K_RIGHT] - keys[pygame.K_LEFT],
            keys[pygame.K_DOWN] - keys[pygame.K_UP]
        ]

        self.position = tuple(sum(x) for x in zip(self.position, (keys_input * dt) * 12))
        self.rect = pygame.Rect(self.position, (24, 24))
    def draw(self):
        pygame.draw.rect(screen, (255, 0, 0), self.rect)

class Tile:
    def __init__(self, position):
        self.rect = pygame.Rect(position, (24, 24))
    def tick(self, dt):
        pass
    def draw(self):
        pygame.draw.rect(screen, (0, 255, 0), self.rect)

pygame.init() 

#Create screen surface 
screen = pygame.display.set_mode((480, 360)) 
pygame.display.set_caption("Collision... Probably?") 

#Create game, start game loop
game = Game(screen)
while game.running: 
    game.handle_events()
    game.tick()
    game.draw()