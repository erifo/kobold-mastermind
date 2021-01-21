import pygame

class View():
    def __init__(self, model, screen):
        self.model = model
        self.screen = screen

    def update(self):
        self.draw()
        
    def draw(self):
        self.screen.fill((0,0,0))
        # ...
        pygame.display.flip()