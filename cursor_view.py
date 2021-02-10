import pygame

class CursorView():
    def __init__(self, screen):
        self.screen = screen

    def draw(self, x, y, model, size):
        pygame.draw.rect(self.screen, (255,0,0), (x,y,size,size), 3)