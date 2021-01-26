from game_model import GameModel
from game_view import GameView
from game_controller import GameController

def main():
    model = GameModel()
    view = GameView(800, 600)
    controller = GameController(model, view)
    # ---
    while (True):
        controller.update()

if __name__ == "__main__":
    main()
