from floor_model import FloorModel
from guesses_model import GuessesModel
from states import States

class PlayModel():
    def __init__(self):
        self.floor = FloorModel(9,3)
        self.guesses = GuessesModel(5,10)
    
    def move_cursor_up(self):
        self.floor.move_cursor(0,-1)

    def move_cursor_down(self):
        self.floor.move_cursor(0,1)

    def move_cursor_left(self):
        self.floor.move_cursor(-1,0)

    def move_cursor_right(self):
        self.floor.move_cursor(1,0)

    def toggle_cursor_carry(self):
        self.floor.toggle_cursor_carry()

    def make_guess(self, state_manager):
        if not self.floor.are_circles_filled():
            return # Do nothing.
        if self.floor.is_guess_correct():
            state_manager.push(States.WIN)
        else:
            pass # Lower ceiling.
        guess = self.floor.create_guess()
        self.guesses.add_guess(guess)