"""Centered menu for ShellSpaceInvaders."""

import msvcrt
import os
import shutil

from constants import WIDTH


OPTIONS = ["Play", "Instructions", "Quit"]


def _key():
    key = msvcrt.getch()
    if key in (b"\x00", b"\xe0"):
        return {b"H": "UP", b"P": "DOWN"}.get(msvcrt.getch(), "")
    if key in (b"w", b"W"):
        return "UP"
    if key in (b"s", b"S"):
        return "DOWN"
    if key in (b"\r", b"\n"):
        return "ENTER"
    if key in (b"q", b"Q", b"\x1b"):
        return "QUIT"
    return ""


def _show(block):
    columns, rows = shutil.get_terminal_size((80, 24))
    lines = block.splitlines()
    print("\n" * max(0, (rows - len(lines)) // 2))
    print("\n".join(line.center(columns) for line in lines))


def choose():
    selected = 0
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        lines = ["=" * WIDTH, "SHELL SPACE INVADERS".center(WIDTH), "=" * WIDTH, ""]
        lines += [("> " if i == selected else "  ") + option for i, option in enumerate(OPTIONS)]
        lines += ["", "Use W/S or Up/Down, Enter to select"]
        _show("\n".join(lines))
        key = _key()
        if key == "UP":
            selected = (selected - 1) % len(OPTIONS)
        elif key == "DOWN":
            selected = (selected + 1) % len(OPTIONS)
        elif key == "ENTER":
            return OPTIONS[selected]
        elif key == "QUIT":
            return "Quit"
