from menu_model import MenuModel
from menu_option import MenuOption
from play_model import PlayModel
from states import States

"""
    Contains all lesser models.
"""

class GameModel():
    def __init__(self):
        self.menu = MenuModel(MenuOption("New Game", States.PLAY),
                               MenuOption("Continue", States.CONTINUE),
                               MenuOption("Exit", States.EXIT))
        self.play = PlayModel()