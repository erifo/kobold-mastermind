from game_model import GameModel
from game_view import GameView
from game_controller import GameController

def main():
    model = GameModel() # Holds gamedata and business logic
    view = GameView(800, 600) # Holds display-data and drawing-methods
    controller = GameController(model, view) # Updates model, orders view.
    # ---
    while (True):
        controller.update()

if __name__ == "__main__":
    main()
