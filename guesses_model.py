class GuessesModel():
    def __init__(self, columns, rows):
        self.columns = columns
        self.rows = rows
        self.guesses = []
    
    def add_guess(self, guess):
        if self.get_nr_of_guesses() >= self.rows:
            return
        self.guesses.append(guess)
    
    def get_guess_at(self, i):
        return self.guesses[i]
    
    def get_nr_of_guesses(self):
        return len(self.guesses)