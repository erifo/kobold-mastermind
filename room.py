from circle import Circle

class Room():
    def __init__(self, height, width, wall_length, nrOfCircles):
        self.height = height              # cells
        self.width = width                # cells
        self.wall_length = wall_length    # feet
        self.circles = self.initCircles(nrOfCircles)
    

    def initCircles(self, amount):
        circles = []
        for i in range(amount):
            y = self.height//2
            x = self.width//amount*i
            circles.append(Circle(y,x,i))
        return circles
