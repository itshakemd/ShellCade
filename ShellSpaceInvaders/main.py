"""ShellSpaceInvaders entry point."""

import os

from game import InvadersGame
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
        game = InvadersGame()
        if not run_game(game):
            continue
        os.system("cls" if os.name == "nt" else "clear")
        print("GAME OVER")
        print(f"Final score: {game.score}   Wave: {game.wave}")
        input("Press Enter to return to menu...")


if __name__ == "__main__":
    main()
