"""ShellPong application entry point."""

from menu import choose_mode
from pong import PongGame
from loop import run_game


def main():
    while True:
        mode = choose_mode()
        if mode is None:
            print("Thanks for playing ShellPong!")
            return
        game = PongGame(two_player=mode)
        if not run_game(game):
            return
        print(f"Final score: {game.left_score} - {game.right_score}")
        input("Press Enter to return to the menu...")


if __name__ == "__main__":
    main()
