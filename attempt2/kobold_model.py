class KoboldModel():
    def __init__(self, x, y, cid):
        self.x = x
        self.y = y
        self.cid = cid
    
    def move(self, xmod, ymod):
        self.x += xmod
        self.y += ymod