import pygame, sys
from state_manager import StateManager
from states import States


class GameController():
    def __init__(self, model, view):
        pygame.init()
        self.model = model
        self.view = view
        self.state_manager = StateManager()

    
    def update(self):
        for event in pygame.event.get():
            if (event.type == pygame.KEYDOWN):
                state = self.state_manager.current()
                if state == States.MENU:
                    if (event.key == pygame.K_UP):
                        pass
                    elif (event.key == pygame.K_DOWN):
                        pass
                    elif (event.key == pygame.K_SPACE):
                        pass
                    self.view.draw_menu(self.model.menu)
                elif state == States.GAME:
                    pass
                elif state == States.WIN:
                    pass
                elif state == States.LOSE:
                    pass
            elif (event.type == pygame.QUIT):
                sys.exit()