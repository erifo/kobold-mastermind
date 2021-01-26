import pygame
from menu_view import MenuView
from play_view import PlayView

"""
    Contains all lesser views.
"""

class GameView():
    def __init__(self, width, height):
        pygame.font.init()
        pygame.display.set_caption("Kobold Mastermind")
        self.font = pygame.font.Font("snesfont.ttf", 40)
        self.WIDTH = width
        self.HEIGHT = height
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.menu = MenuView(300, 200, self.screen, self.WIDTH, self.HEIGHT, self.font)
        self.play = PlayView(self.screen, self.WIDTH, self.HEIGHT, self.font)

    def draw_menu(self, model):
        self.menu.draw(model)
    
    def draw_play(self, model):
        self.play.draw(model)