import pygame
from floor_view import FloorView

class PlayView():
    def __init__(self, screen, window_width, window_height, font):
        self.screen = screen
        self.font = font # Remove when instancing HUD class using font later.
        self.floor = FloorView(300, 100, screen, window_width, window_height)

    def draw(self, model):
        self.screen.fill((0,0,0))
        self.floor.draw(model.floor)
        #self.wall.draw(model.wall)
        #self.guesses.draw(model.guesses)