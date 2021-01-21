class Selection():
    def __init__(self, options):
        self.options = options
        self.selected = 0
    
    def selectPrevious(self):
        if (self.selected-1 < 0):
            return
        self.selected -= 1
    
    def selectNext(self):
        if (self.selected+1 >= len(self.options)):
            return
        self.selected += 1
    
    def getSelected(self):
        return self.options[self.selected]