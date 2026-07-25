"""Centered menu for ShellFlappyBird."""

import msvcrt
import shutil

from blessed import Terminal


OPTIONS = ["Play", "Instructions", "Quit"]


def _center(text):
    columns, rows = shutil.get_terminal_size((80, 24))
    lines = text.splitlines()
    return "\n" * max(0, (rows - len(lines)) // 2) + "\n".join(
        line.center(columns) for line in lines
    )


def choose():
    selected = 0
    term = Terminal()
    while True:
        lines = ["=" * 32, "SHELL FLAPPY BIRD".center(32), "=" * 32, ""]
        lines += [("> " if i == selected else "  ") + option for i, option in enumerate(OPTIONS)]
        lines += ["", "Use W/S or Up/Down, Enter to select"]
        print(term.home + term.clear + term.bold_yellow(_center("\n".join(lines))))
        key = msvcrt.getch()
        if key in (b"w", b"W", b"\x00H"):
            selected = (selected - 1) % len(OPTIONS)
        elif key in (b"s", b"S", b"\x00P"):
            selected = (selected + 1) % len(OPTIONS)
        elif key in (b"\r", b"\n"):
            return OPTIONS[selected]
        elif key in (b"q", b"Q", b"\x1b"):
            return "Quit"
