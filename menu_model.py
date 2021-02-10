class MenuModel():
    def __init__(self, *options):
        self.options = options
        self.selected = 0
    
    def select_previous(self):
        if (self.selected-1 < 0):
            return
        self.selected -= 1
    
    def select_next(self):
        if (self.selected+1 >= len(self.options)):
            return
        self.selected += 1
    
    def _get_option_at(self, i):
        return self.options[i]

    def _get_option_selected(self):
        return self._get_option_at(self.selected)

    def get_option_text_at(self, i):
        return self._get_option_at(i).text
    
    def get_option_selected_state(self):
        return self._get_option_selected().state