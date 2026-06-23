"""Windows terminal Snake entry point."""

import os
import sys

from game_loop import run_game
from menu import show_high_score_screen, show_instructions_screen, show_menu
from scores import load_scores, top_score


def main():
    scores = load_scores()
    while True:
        high_score_name, high_score = top_score(scores)
        choice = show_menu(high_score_name, high_score)
        if choice == "Play":
            scores = run_game(scores)
        elif choice == "High Score":
            show_high_score_screen(scores)
        elif choice == "Instructions":
            show_instructions_screen()
        elif choice == "Quit":
            os.system("cls" if os.name == "nt" else "clear")
            print("Thanks for playing Snake!")
            break


if __name__ == "__main__":
    if os.name != "nt":
        print("This game uses msvcrt and only runs on Windows.")
        sys.exit(1)
    main()
