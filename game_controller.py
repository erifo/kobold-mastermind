import pygame, sys
from state_manager import StateManager
from states import States


class GameController():
    def __init__(self, model, view):
        pygame.init()
        self.model = model
        self.view = view
        self.state_manager = StateManager()
        self.state_manager.push(States.MENU)

    
    def update(self):
        state = self.state_manager.current()
        events = pygame.event.get()
        keyboard_events = [e for e in events if e.type == pygame.KEYDOWN]
        # ---
        if state == States.MENU:
            self.handle_menu(keyboard_events)
            self.view.draw_menu(self.model.menu)
        elif state == States.PLAY:
            self.handle_play(keyboard_events)
            self.view.draw_play(self.model.play)
        elif state == States.CONTINUE:
            pass
        elif state == States.WIN:
            self.view.draw_win()
        elif state == States.LOSE:
            pass
        elif state == States.EXIT:
            self.handle_exit()
        # ---
        for event in events:
            if event.type == pygame.QUIT:
                sys.exit()
        pygame.display.flip()


    def handle_menu(self, keyboard_events):
        menu = self.model.menu
        for event in keyboard_events:
            if (event.key == pygame.K_UP):
                menu.select_previous()
            elif (event.key == pygame.K_DOWN):
                menu.select_next()
            elif (event.key == pygame.K_SPACE):
                selected_state = menu.get_option_selected_state()
                self.state_manager.push(selected_state)
    
    def handle_play(self, keyboard_events):
        play = self.model.play
        for event in keyboard_events:
            if (event.key == pygame.K_UP):
                play.move_cursor_up()
            elif (event.key == pygame.K_DOWN):
                play.move_cursor_down()
            elif (event.key == pygame.K_LEFT):
                play.move_cursor_left()
            elif (event.key == pygame.K_RIGHT):
                play.move_cursor_right()
            elif (event.key == pygame.K_SPACE):
                play.toggle_cursor_carry()
            elif (event.key == pygame.K_RETURN):
                play.make_guess(self.state_manager)

    def handle_continue(self, keyboard_events):
        pass

    def handle_win(self, keyboard_events):
        pass

    def handle_lose(self, keyboard_events):
        pass

    def handle_exit(self):
        sys.exit()