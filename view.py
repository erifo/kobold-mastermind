import pygame
from gamestates import Gamestates

class View():
    def __init__(self, model, screen):
        self.model = model
        self.screen = screen

    def update(self):
        self.draw()
        
    def draw(self):
        self.screen.fill((0,0,0))
        if (self.model.state == Gamestates.MENU):
            self.drawMenu()
        elif (self.model.state == Gamestates.GAMEPLAY):
            self.drawGameplay()
        elif (self.model.state == Gamestates.WIN):
            self.drawWin()
        elif (self.model.state == Gamestates.LOSE):
            self.drawLose()
        pygame.display.flip()
    
    def drawMenu(self):
        height = 200
        width = 300
        y = (self.model.height//2) - (height//2)
        x = (self.model.width//2) - (width//2)
        pygame.draw.rect(self.screen, (50,50,200), (x,y,width,height), 0, 10)
        for i in range(len(self.model.menu.options)):
            text = self.model.menu.options[i].text
            if (self.model.menu.selected == i):
                text = '[ '+text+' ]'
            textSize = self.model.font.size(text)
            ty = y + (textSize[1]*i) + 50
            tx = x + (width//2) - (textSize[0]//2)
            textSurface = self.model.font.render(text, False, (255,255,255))
            self.screen.blit(textSurface, (tx, ty))

    def drawGameplay(self):
        self.drawRoom()
        self.drawRecord()
        self.drawKobolds()
        self.drawCursor()

    def drawRoom(self):
        height = self.model.height//10*6
        width = (self.model.width//10*4)
        y = (self.model.height//10*2)
        x = (self.model.width//10*5) + 10
        pygame.draw.rect(self.screen, (70,70,70), (x,y,width,height), 0, 5)

    def drawRecord(self):
        height = (self.model.height//10*6)
        width = (self.model.width//10*4)
        y = (self.model.height//10*2)
        x = (self.model.width//10) - 10
        pygame.draw.rect(self.screen, (200,50,50), (x,y,width,height), 5, 10)

    def drawKobolds(self):
        pass

    def drawCursor(self):
        pass

    def drawWin(self):
        pass

    def drawLose(self):
        pass