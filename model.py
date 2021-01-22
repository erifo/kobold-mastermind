import pygame, sys
from gamestates import Gamestates
from selection import Selection
from option import Option
from room import Room

class Model(): 
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.font = pygame.font.Font("snesfont.ttf", 40)
        self.state = Gamestates.MENU
        self.menu = Selection([Option("New Game", Gamestates.GAMEPLAY),
                               Option("Continue", Gamestates.GAMEPLAY),
                               Option("Exit", Gamestates.EXIT)])
        self.room = Room(3,9,20,4)
    
    def menuSelect(self):
        self.state = self.menu.getSelected().state
    
    def update(self):
        if (self.state == Gamestates.GAMEPLAY):
            self.updateGameplay()
        elif (self.state == Gamestates.MENU):
            pass
        elif (self.state == Gamestates.WIN):
            pass
        elif (self.state == Gamestates.LOSE):
            pass
        elif (self.state == Gamestates.EXIT):
            sys.exit()
    
    def updateGameplay(self):
        pass