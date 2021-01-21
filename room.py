from circle import Circle

class Room():
    def __init__(self, height, width, height, nrOfCircles):
        self.height = height    # cells
        self.width = width      # cells
        self.height = height    # feet
        self.circles = initCircles(nrOfCircles)
    

    def initCircles(self, amount):
        circles = []
        for i in range(amount):
            y = self.height//2
            x = self.width//amount*i
            circles.append(Circle(y,x,i))
        return circles
