from random import shuffle
from circle_model import CircleModel
from kobold_model import KoboldModel
from cursor_model import CursorModel
from guess_model import GuessModel

class FloorModel():
    def __init__(self, columns, rows):
        self.columns = columns
        self.rows = rows
        self.circles = self.init_circles(4)
        self.kobolds = self.init_kobolds(4)
        self.cursor = CursorModel(0, 0)
    
    def init_circles(self, amount):
        circles = []
        for i in range(amount):
            x = (self.columns//amount*i) + 1
            y = self.rows//2
            circle_id = i # Circle Identification
            circles.append(CircleModel(x,y,circle_id))
        return circles

    def init_kobolds(self, amount):
        kobolds = []
        circle_ids = [i for i in range(amount)]
        shuffle(circle_ids)
        for i in range(amount):
            #x = i
            #y = self.rows-1
            x = (self.columns//amount*i) + 1 #DEBUG
            y = self.rows//2 #DEBUG
            circle_id = circle_ids[i] # The circle that kobold belongs to.
            color_id = i
            kobolds.append(KoboldModel(x,y,circle_id, color_id))
        return kobolds
    
    def is_kobold_at(self, x, y):
        for kobold in self.kobolds:
            if x == kobold.x and y == kobold.y:
                return True
        return False
    
    def get_kobold_at(self, x, y):
        for kobold in self.kobolds:
            if x == kobold.x and y == kobold.y:
                return kobold
        return None
    
    def is_circle_at(self, x, y):
        for circle in self.circles:
            if x == circle.x and y == circle.y:
                return True
        return False
    
    def get_circle_at(self, x, y):
        for circle in self.circles:
            if x == circle.x and y == circle.y:
                return circle
        return None
    
    def is_cursor_at(self, x, y):
        if x == self.cursor.x and y == self.cursor.y:
            return True
        return False
    
    def is_in_grid(self, x, y):
        if (x < 0 or x >= self.columns):
            return False
        if (y < 0 or y >= self.rows):
            return False
        return True
    
    def move_cursor(self, xmod, ymod):
        xnew = self.cursor.x + xmod
        ynew = self.cursor.y + ymod
        if not self.is_in_grid(xnew, ynew):
            return
        if self.cursor.carrying:
            if self.is_kobold_at(xnew, ynew):
                return
            kobold = self.get_kobold_at(self.cursor.x, self.cursor.y)
            kobold.move(xmod, ymod)
        self.cursor.move(xmod, ymod)

    def toggle_cursor_carry(self):
        if self.cursor.carrying:
            self.cursor.carrying = False
        elif self.is_kobold_at(self.cursor.x, self.cursor.y):
            self.cursor.carrying = True

    def are_circles_filled(self):
        for circle in self.circles:
            filled = False
            for kobold in self.kobolds:
                if (kobold.x == circle.x and kobold.y == circle.y):
                    filled = True
            if not filled:
                return False
        return True
    
    def is_guess_correct(self):
        for circle in self.circles:
            kobold = self.get_kobold_at(circle.x, circle.y)
            if not circle.circle_id == kobold.circle_id:
                return False
        return True
    
    def get_currently_correct_amount(self):
        counter = 0
        for circle in self.circles:
            kobold = self.get_kobold_at(circle.x, circle.y)
            if circle.circle_id == kobold.circle_id:
                counter += 1
        return counter
    
    def get_kobold_order(self):
        kobolds = []
        for circle in self.circles:
            kobold = self.get_kobold_at(circle.x, circle.y)
            kobolds.append(kobold)
        return kobolds

    def create_guess(self):
        nr_of_correct = self.get_currently_correct_amount()
        kobold_order = self.get_kobold_order()
        return GuessModel(str(nr_of_correct), kobold_order)