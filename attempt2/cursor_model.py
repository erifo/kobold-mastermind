class CursorModel():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.carrying = False
    
    def move(self, xmod, ymod):
        self.x += xmod
        self.y += ymod