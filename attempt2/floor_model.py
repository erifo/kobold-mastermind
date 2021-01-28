from random import shuffle
from circle_model import CircleModel
from kobold_model import KoboldModel
from cursor_model import CursorModel

class FloorModel():
    def __init__(self, columns, rows):
        self.columns = columns
        self.rows = rows
        self.circles = self.init_circles(4)
        self.kobolds = self.init_kobolds(4)
        self.cursor = CursorModel(0, 0)
    
    def init_circles(self, amount):
        circles = []
        cids = [i for i in range(amount)]
        shuffle(cids)
        for i in range(amount):
            x = (self.columns//amount*i) + 1
            y = self.rows//2
            cid = cids[i] # Circle Identification
            circles.append(CircleModel(x,y,cid))
        return circles

    def init_kobolds(self, amount):
        kobolds = []
        for i in range(amount):
            x = i
            y = self.rows-1
            cid = i # Circle Identification (for kobold)
            kobolds.append(KoboldModel(x,y,cid))
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
