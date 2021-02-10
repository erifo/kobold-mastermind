import pygame

class MenuView():
    def __init__(self, menu_width, menu_height, screen, window_width, window_height, font):
        self.menu_width = menu_width
        self.menu_height = menu_height
        self.screen = screen
        self.window_width = window_width
        self.window_height = window_height
        self.font = font

    def draw(self, model):
        x = (self.window_width//2) - (self.menu_width//2)
        y = (self.window_height//2) - (self.menu_height//2)
        # ---
        self.screen.fill((0,0,0))
        pygame.draw.rect(self.screen, (50,50,200), (x,y,self.menu_width,self.menu_height), 0, 10)
        for i in range(len(model.options)):
            text = model.get_option_text_at(i)
            if (model.selected == i):
                text = '[ '+text+' ]'
            text_width, text_height = self.font.size(text)
            ty = y + (text_height*i) + 50
            tx = x + (self.menu_width//2) - (text_width//2)
            textSurface = self.font.render(text, False, (255,255,255))
            self.screen.blit(textSurface, (tx, ty))