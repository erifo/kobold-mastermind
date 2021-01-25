import pygame
from menu_view import MenuView

class GameView():
    def __init__(self, width, height):
        pygame.font.init()
        pygame.display.set_caption("Kobold Mastermind")
        self.WIDTH = width
        self.HEIGHT = height
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.menu = MenuView()

    def draw_menu(self, model):
        self.menu.draw(model, self.screen)