import pygame

class KoboldView():
    def __init__(self, screen):
        self.colors = [(255,50,50), (50,255,50), (50,50,255), (255,50,255)]
        self.screen = screen
        self.size = 10

    def draw(self, x, y, model):
        pygame.draw.rect(self.screen, self.colors[model.cid], (x,y,self.size,self.size))