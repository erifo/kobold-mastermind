import sys, pygame
from gamestates import Gamestates


class Controller():
    def __init__(self, model):
        self.model = model

    def update(self):
       for event in pygame.event.get():
            if (event.type == pygame.KEYDOWN):
                if (model.state == Gamestates.GAMEPLAY):
                    if (event.key == pygame.K_UP):
                        pass
                    elif (event.key == pygame.K_DOWN):
                        pass
                    elif (event.key == pygame.K_LEFT):
                        pass
                    elif (event.key == pygame.K_DOWN):
                        pass
                if (model.state == Gamestates.MAIN_MENU):
                    if (event.key == pygame.K_UP):
                        pass
                    elif (event.key == pygame.K_DOWN):
                        pass
                    elif (event.key == pygame.K_SPACE):
                        pass
                if (model.state == Gamestates.WIN):
                    if (event.key == pygame.K_SPACE):
                        pass
                if (model.state == Gamestates.LOSE):
                    if (event.key == pygame.K_SPACE):
                        pass
            if (event.type == pygame.QUIT):
                sys.exit()