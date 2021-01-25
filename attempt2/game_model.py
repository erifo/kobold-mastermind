from menu_model import MenuModel
from menu_option import MenuOption
from states import States

class GameModel():
    def __init__(self):
        self.menu = MenuModel([MenuOption("New Game", States.GAME),
                               MenuOption("Continue", States.CONTINUE),
                               MenuOption("Exit", States.EXIT)])