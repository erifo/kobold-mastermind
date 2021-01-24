from circle import Circle
from kobold import Kobold

class Room():
    def __init__(self, height, width, wall_length, nrOfCircles):
        self.height = height              # cells
        self.width = width                # cells
        self.wall_length = wall_length    # feet
        self.circles = self.initCircles(nrOfCircles)
        self.kobolds = self.initKobolds(nrOfCircles) # To get equal amount.
    

    def initCircles(self, amount):
        circles = []
        for i in range(amount):
            y = self.height//2
            x = self.width//amount*i
            circles.append(Circle(y,x,i))
        return circles

    def initKobolds(self, amount):
        kobolds = []
        for i in range(amount):
            y = height-1
            x = 0+i # Gets them lined up from the left wall.
            kobolds.append(Kobold(y,x,i))