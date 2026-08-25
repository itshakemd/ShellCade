"""Tic-Tac-Toe application entrypoint."""

from blessed import Terminal

from .loop import run_game
from .menu import choose, show_instructions


def main() -> None:
    term = Terminal()
    while True:
        choice = choose()
        if choice == "Quit":
            return
        if choice == "Instructions":
            show_instructions()
        else:
            run_game(term, choice == "Single Player")


if __name__ == "__main__":
    main()
