import pygame

class FloorView():
    def __init__(self, floor_width, floor_height, screen, window_width, window_height):
        self.floor_width = floor_width
        self.floor_height = floor_height
        self.screen = screen
        self.window_width = window_width
        self.window_height = window_height
    
    def draw(self, model):
        x = ((self.window_width//4)*3) - (self.floor_width//2)
        y = ((self.window_height//4)) - (self.floor_height//2)
        # ---
        # TEMP
        pygame.draw.rect(self.screen, (50,200,50), (x,y,self.floor_width,self.floor_height), 2)
        