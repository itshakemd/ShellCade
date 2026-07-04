"""Main menu and instructions screen for ShellPong."""

import msvcrt
import os
import shutil

from constants import WIDTH


OPTIONS = ["Single Player", "Two Players", "Instructions", "Quit"]


def _clear():
    os.system("cls" if os.name == "nt" else "clear")


def _center(text):
    columns, rows = shutil.get_terminal_size((80, 24))
    lines = text.splitlines()
    top_padding = max(0, (rows - len(lines)) // 2)
    return "\n" * top_padding + "\n".join(
        line.center(columns) for line in lines
    )


def _read_menu_key():
    key = msvcrt.getch()
    if key in (b"\x00", b"\xe0"):
        arrow = msvcrt.getch()
        return {b"H": "UP", b"P": "DOWN"}.get(arrow, "")
    if key in (b"w", b"W"):
        return "UP"
    if key in (b"s", b"S"):
        return "DOWN"
    if key in (b"\r", b"\n"):
        return "ENTER"
    if key in (b"q", b"Q", b"\x1b"):
        return "QUIT"
    return ""


def _draw_menu(selected):
    width = WIDTH
    lines = [
        "=" * width,
        "SHELLPONG".center(width),
        "=" * width,
        "",
    ]
    for index, option in enumerate(OPTIONS):
        marker = "> " if index == selected else "  "
        lines.append((marker + option).center(width))
    lines.extend(["", "Use W/S or Up/Down, Enter to select".center(width)])
    return "\n".join(lines)


def choose_mode():
    selected = 0
    while True:
        _clear()
        print(_center(_draw_menu(selected)))
        key = _read_menu_key()
        if key == "UP":
            selected = (selected - 1) % len(OPTIONS)
        elif key == "DOWN":
            selected = (selected + 1) % len(OPTIONS)
        elif key == "ENTER":
            if OPTIONS[selected] == "Single Player":
                return False
            if OPTIONS[selected] == "Two Players":
                return True
            if OPTIONS[selected] == "Instructions":
                show_instructions()
            else:
                return None
        elif key == "QUIT":
            return None


def show_instructions():
    _clear()
    block = "\n".join([
        "SHELLPONG INSTRUCTIONS",
        "-" * WIDTH,
        "Single Player: W / S move Player 1",
        "Two Players:   W / S move P1, Up / Down move P2",
        "P              pause or resume the match",
        "Q              quit to the menu",
        "",
        "The first player to reach seven points wins.",
        "",
        "Press any key to return to the menu",
    ])
    print(_center(block))
    msvcrt.getch()
