import pygame
from model import Model
from view import View
from controller import Controller

class Game():
    def __init__(self, height, width):
        pygame.init()
        pygame.font.init()
        pygame.display.set_caption("Kobold Mastermind")
        self.screen = pygame.display.set_mode((width, height))
        # -----
        self.model = Model(height, width)
        self.view = View(self.model, self.screen)
        self.controller = Controller(self.model)

    def update(self):
        self.controller.update()
        self.model.update()
        self.view.update()
    
    def start(self):
        while(True):
            self.update()