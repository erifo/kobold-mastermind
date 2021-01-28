from floor_model import FloorModel

class PlayModel():
    def __init__(self):
        self.floor = FloorModel(9,3)
    
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