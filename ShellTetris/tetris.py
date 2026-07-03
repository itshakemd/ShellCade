"""
Terminal Tetris for Windows (uses msvcrt for non-blocking keyboard input).

Main Menu:
  W/S or Up/Down  - navigate menu
  Enter           - select

In-Game Controls:
  A / D      - move left / right
  S          - soft drop
  W or Up*   - rotate  (*arrow keys also work)
  Space      - hard drop
  P          - pause
  Q          - quit to menu

This file is the entry point. The game itself is split across a few
modules that must sit in the same folder as this file:
  constants.py    - board size, high-score file path, piece shapes
  piece.py        - the falling Piece and the 7-bag randomizer
  game.py         - the Game class (board, rules, scoring, rendering)
  scores.py       - leaderboard persistence
  display.py      - clear_screen / center text helpers
  keyboard_input.py - msvcrt-based key reading and text entry
  menu.py         - main menu and info screens
  game_loop.py    - the live gameplay loop
"""

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
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    if os.name != "nt":
        print("This game uses msvcrt and only runs on Windows.")
        sys.exit(1)
    main()
