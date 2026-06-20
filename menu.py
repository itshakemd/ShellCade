"""Main menu and informational screens (leaderboard, instructions)."""

import msvcrt

from constants import WIDTH
from display import clear_screen, print_centered
from keyboard_input import read_key
from scores import format_leaderboard_line


def draw_menu(selected, high_score_name, high_score):
    width = WIDTH * 2 + 2
    lines = []
    lines.append("=" * width)
    lines.append("TETRIS".center(width))
    lines.append("=" * width)
    lines.append("")
    lines.append(f"High Score: {high_score_name} - {high_score}".center(width))
    lines.append("")
    options = ["Play", "High Score", "Instructions", "Quit"]
    for i, opt in enumerate(options):
        marker = "> " if i == selected else "  "
        lines.append((marker + opt).center(width))
    lines.append("")
    lines.append("Use W/S or Up/Down, Enter to select".center(width))
    return "\n".join(lines)


def show_menu(high_score_name, high_score):
    options = ["Play", "High Score", "Instructions", "Quit"]
    selected = 0
    while True:
        clear_screen()
        print_centered(draw_menu(selected, high_score_name, high_score))
        key = read_key()
        if key == "UP":
            selected = (selected - 1) % len(options)
        elif key == "DOWN":
            selected = (selected + 1) % len(options)
        elif key == "ENTER":
            return options[selected]
        elif key == "ESC":
            return "Quit"

