import pygame
from floor_view import FloorView
from guesses_view import GuessesView

class PlayView():
    def __init__(self, screen, window_width, window_height, font):
        self.screen = screen
        self.floor = FloorView(300, 100, screen, window_width, window_height)
        self.guesses = GuessesView(300, 300, screen, window_width, window_height, font)

    def draw(self, model):
        self.screen.fill((0,0,0))
        self.floor.draw(model.floor)
        self.guesses.draw(model.guesses)
        #self.wall.draw(model.wall)