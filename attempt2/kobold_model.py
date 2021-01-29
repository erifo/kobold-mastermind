class KoboldModel():
    def __init__(self, x, y, circle_id, color_id):
        self.x = x
        self.y = y
        self.circle_id = circle_id
        self.color_id = color_id
    
    def move(self, xmod, ymod):
        self.x += xmod
        self.y += ymod