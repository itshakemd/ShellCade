"""Main menu and informational screens for Snake."""

import msvcrt

from constants import WIDTH
from display import clear_screen, print_centered
from keyboard_input import read_key
from scores import format_leaderboard_line


def draw_menu(selected, high_score_name, high_score):
    width = WIDTH * 2 + 2
    lines = [
        "=" * width,
        "SNAKE".center(width),
        "=" * width,
        "",
        f"High Score: {high_score_name} - {high_score}".center(width),
        "",
    ]
    options = ["Play", "High Score", "Instructions", "Quit"]
    for i, option in enumerate(options):
        marker = "> " if i == selected else "  "
        lines.append((marker + option).center(width))
    lines.extend(["", "Use W/S or Up/Down, Enter to select".center(width)])
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


def show_high_score_screen(scores):
    clear_screen()
    width = max(WIDTH * 2 + 2, 28)
    lines = ["=" * width, "LEADERBOARD".center(width), "=" * width, ""]
    if not scores:
        lines.append("No scores yet".center(width))
    else:
        for i, (name, score) in enumerate(scores, start=1):
            lines.append(format_leaderboard_line(i, name, score, width))
    lines.extend(["", "Press any key to go back".center(width)])
    print_centered("\n".join(lines))
    msvcrt.getch()


def show_instructions_screen():
    clear_screen()
    block = "\n".join([
        "INSTRUCTIONS",
        "-" * 40,
        "Arrows or W/A/S/D - steer the snake",
        "P                 - pause / resume",
        "Q                 - quit to menu",
        "",
        "Eat the fruit to grow and score 10 points.",
        "Avoid the walls and your own tail.",
        "The snake speeds up every 50 points.",
        "",
        "Press any key to go back",
    ])
    print_centered(block)
    msvcrt.getch()
