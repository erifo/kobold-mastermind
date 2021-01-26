from circle_model import CircleModel
from kobold_model import KoboldModel
from cursor_model import CursorModel

class FloorModel():
    def __init__(self, columns, rows):
        self.columns = columns
        self.rows = rows
        self.circles = self.init_circles(4)
        self.kobolds = self.init_kobolds(4)
        self.cursor = CursorModel(self.columns//2, self.rows//2)
    
    def init_circles(self, amount):
        circles = []
        for i in range(amount):
            x = self.columns//amount
            y = self.rows//2
            cid = i # Circle Identification
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