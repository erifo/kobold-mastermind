from enum import Enum

class States(Enum):
    MENU = 0
    GAME = 1
    CONTINUE = 2
    WIN = 3
    LOSE = 4
    EXIT = 5