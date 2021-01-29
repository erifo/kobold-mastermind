import pygame
from kobold_view import KoboldView
from circle_view import CircleView
from cursor_view import CursorView

class FloorView():
    def __init__(self, floor_width, floor_height, screen, window_width, window_height):
        self.floor_width = floor_width
        self.floor_height = floor_height
        self.screen = screen
        self.window_width = window_width
        self.window_height = window_height
        self.kobold_view = KoboldView(self.screen) #Reused to draw each kobold.
        self.circle_view = CircleView(self.screen) #Reused to draw each circle.
        self.cursor_view = CursorView(self.screen)

    def draw(self, model):
        x = ((self.window_width//2)) - (self.floor_width//2)
        y = ((self.window_height//4)*3) - (self.floor_height//2)
        cell_size = self.floor_width//model.columns
        # ---
        # Grid
        for i in range(1, model.columns):
            start = (x+(i*cell_size), y)
            end = (x+(i*cell_size), y+self.floor_height)
            pygame.draw.line(self.screen, (50,200,50), start, end, width=2)
        for i in range(1, model.rows):
            start = (x, y+(i*cell_size))
            end = (x+self.floor_width, y+(i*cell_size))
            pygame.draw.line(self.screen, (50,200,50), start, end, width=2)
        # ---
        # Border
        pygame.draw.rect(self.screen, (50,200,50), (x,y,self.floor_width,self.floor_height), 2)
        # ---
        # Circles
        for column in range(model.columns):
            for row in range(model.rows):
                if model.is_circle_at(column, row):
                    circle = model.get_circle_at(column, row)
                    cx = x + (circle.x * cell_size) + (cell_size//2) #(self.circle_view.radius//2)
                    cy = y + (circle.y * cell_size) + (cell_size//2) #(self.circle_view.radius//2)
                    self.circle_view.draw(cx, cy, circle)
        # ---
        # Kobolds
        for column in range(model.columns):
            for row in range(model.rows):
                if model.is_kobold_at(column, row):
                    kobold = model.get_kobold_at(column, row)
                    kx = x + kobold.x * cell_size + (cell_size//2) - (self.kobold_view.size//2)
                    ky = y + kobold.y * cell_size + (cell_size//2) - (self.kobold_view.size//2)
                    self.kobold_view.draw(kx, ky, kobold)
        # ---
        # Cursor
        for column in range(model.columns):
            for row in range(model.rows):
                if model.is_cursor_at(column, row):
                    cursor = model.cursor
                    cx = x + cursor.x * cell_size
                    cy = y + cursor.y * cell_size
                    self.cursor_view.draw(cx, cy, cursor, cell_size)