import pygame
from kobold_view import KoboldView

class GuessesView():
    def __init__(self, table_width, table_height, screen, window_width, window_height, font):
        self.table_width = table_width
        self.table_height = table_height
        self.screen = screen
        self.window_width = window_width
        self.window_height = window_height
        self.font = font
        self.kobold_view = KoboldView(screen)
    
    def draw(self, model):
        x = ((self.window_width//2)) - (self.table_width//2)
        y = ((self.window_height//4)*2) - 75 - (self.table_height//2)
        cell_width = self.table_width//model.columns
        cell_height = self.table_height//model.rows
        # ---
        # Grid
        for i in range(1, model.columns):
            start = (x+(i*cell_width), y)
            end = (x+(i*cell_width), y+self.table_height)
            pygame.draw.line(self.screen, (200,50,50), start, end, width=2)
        for i in range(1, model.rows):
            start = (x, y+(i*cell_height))
            end = (x+self.table_width, y+(i*cell_height))
            pygame.draw.line(self.screen, (200,50,50), start, end, width=2)
        # ---
        # Border
        pygame.draw.rect(self.screen, (200,50,50), (x,y,self.table_width,self.table_height), 2)
        # ---
        # Table Data
        for guess_i in range(model.get_nr_of_guesses()):
            guess = model.get_guess_at(guess_i) 
            # ---
            # Nr of Correctly ordered kobolds.
            text = guess.nr_of_correct
            text_width, text_height = self.font.size(text)
            tx = x + (cell_width//2) - (text_width//2)
            ty = y + (guess_i * cell_height) + (cell_height//2) - (text_height//2)
            textSurface = self.font.render(text, False, (255,255,255))
            self.screen.blit(textSurface, (tx, ty))
            # ---
            # Kobold color order
            for kobold_i in range(1, len(guess.kobolds)+1):
                kobold = guess.kobolds[kobold_i-1]
                kx = x + (kobold_i * cell_width) + (cell_width//2) - (self.kobold_view.size//2)
                ky = y + (guess_i * cell_height) + (cell_height//2) - (self.kobold_view.size//2)
                self.kobold_view.draw(kx, ky, kobold)