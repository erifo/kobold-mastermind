import pygame

class WinView():
    def __init__(self, dialogue_width, dialogue_height, screen, window_width, window_height, font):
        self.dialogue_width = dialogue_width
        self.dialogue_height = dialogue_height
        self.screen = screen
        self.window_width = window_width
        self.window_height = window_height
        self.font = font

    def draw(self):
        x = (self.window_width//2) - (self.dialogue_width//2)
        y = (self.window_height//2) - (self.dialogue_height//2)
        # ---
        self.screen.fill((0,0,0))
        pygame.draw.rect(self.screen, (50,50,200), (x,y,self.dialogue_width,self.dialogue_height), 0, 10)
        text = "A winrar is you!"
        text_width, text_height = self.font.size(text)
        tx = (self.window_width//2) - (text_width//2)
        ty = (self.window_height//2) - (text_height//2)
        textSurface = self.font.render(text, False, (255,255,255))
        self.screen.blit(textSurface, (tx, ty))