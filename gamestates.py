from enum import Enum


class Gamestates(Enum):
    GAMEPLAY = 0
    MENU = 1
    WIN = 2
    LOSE = 3