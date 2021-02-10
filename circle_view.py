import pygame

class CircleView():
    def __init__(self, screen):
        self.screen = screen
        self.radius = 15

    def draw(self, x, y, model):
        pygame.draw.circle(self.screen, (255,255,255), (x,y), self.radius, 2)