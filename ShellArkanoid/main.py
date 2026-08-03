"""Arkanoid application entrypoint."""

from blessed import Terminal

from .loop import run_game
from .menu import show_menu


def main() -> None:
    term = Terminal()
    if show_menu(term):
        run_game(term)


if __name__ == "__main__":
    main()
