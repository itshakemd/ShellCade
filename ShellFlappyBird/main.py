"""ShellFlappyBird entry point."""

from game import FlappyGame
from loop import run_game
from menu import choose, show_instructions


def main():
    while True:
        choice = choose()
        if choice == "Quit":
            return
        if choice == "Instructions":
            show_instructions()
            continue
        game = FlappyGame()
        if not run_game(game):
            continue
        print(f"GAME OVER - Score: {game.score}")
        input("Press Enter to return to menu...")


if __name__ == "__main__":
    main()
