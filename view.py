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
        height = 150 #(self.model.height//10*6)
        width = 300 #(self.model.width//10*4)
        yOrigin = (self.model.height//10*5)
        xOrigin = (self.model.width//10*5) + 10
        room_color = (70,70,70)
        # ---
        # Draws boundary of room.
        pygame.draw.rect(self.screen, room_color, (xOrigin,yOrigin,width,height), 5, 5)
        # ---
        # Draws grid in room, indicating each cell.
        for i in range(1, self.model.room.height):
            yMod = i*(height//self.model.room.height)
            pygame.draw.line(self.screen, room_color, (xOrigin, yOrigin+yMod), (xOrigin+width, yOrigin+yMod), width=2)
        for i in range(1, self.model.room.width):
            xMod = i*(width//self.model.room.width)
            pygame.draw.line(self.screen, room_color, (xOrigin+xMod, yOrigin), (xOrigin+xMod, yOrigin+height), width=2)
        # TODO: Draw circles
        # ---
        # Draw Kobolds
        kobold_colors = [(255,0,0), (0,255,0), (0,0,255), (255,0,255)]
        for i in range(len(self.model.room.kobolds)):
            k = self.model.room.kobolds[i]
            #TODO: Left this unfinished. Need to think this through better.
            pygame.draw.rect(self.screen, kobold_colors[i], (xOrigin,yOrigin,width,height), 5, 5)
        # ---
        # TODO: Draw cursor

    def drawRecord(self):
        height = (self.model.height//10*6)
        width = (self.model.width//10*4)
        yOrigin = (self.model.height//10*2)
        xOrigin = (self.model.width//10) - 10
        record_color = (200,50,50)
        rows = 10
        columns = 5
        # ---
        # Draws boundary of record.
        pygame.draw.rect(self.screen, record_color, (xOrigin,yOrigin,width,height), 5, 10)
        # ---
        # Draws lines separating each guess.
        for i in range(1, rows):
            yMod = i*(height//rows)
            pygame.draw.line(self.screen, record_color, (xOrigin, yOrigin+yMod), (xOrigin+width, yOrigin+yMod), width=2)
        for i in range(1, columns):
            xMod = i*(width//columns)
            pygame.draw.line(self.screen, record_color, (xOrigin+xMod, yOrigin), (xOrigin+xMod, yOrigin+height), width=2)

    def drawWin(self):
        pass

    def drawLose(self):
        pass