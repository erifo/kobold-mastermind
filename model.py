import pygame

class Model(): 
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.font = pygame.font.Font("snesfont.ttf", 40)
        