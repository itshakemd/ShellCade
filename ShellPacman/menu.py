"""Centered Pac-Man menu."""

import msvcrt
import shutil

from blessed import Terminal


OPTIONS = ["Play", "Instructions", "Quit"]


def _center(text: str) -> str:
    columns, rows = shutil.get_terminal_size((80, 24))
    lines = text.splitlines()
    return "\n" * max(0, (rows - len(lines)) // 2) + "\n".join(line.center(columns) for line in lines)


def choose() -> str:
    term = Terminal()
    selected = 0
    while True:
        lines = ["=" * 32, "SHELL PAC-MAN".center(32), "=" * 32, ""]
        lines += [(("> " if i == selected else "  ") + option).center(32) for i, option in enumerate(OPTIONS)]
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


def show_instructions() -> None:
    term = Terminal()
    text = "\n".join([
        "SHELL PAC-MAN INSTRUCTIONS",
        "-" * 32,
        "Arrows or W/A/S/D  move Pac-Man",
        "P                  pause / resume",
        "R                  restart after a round",
        "Q                  quit to menu",
        "",
        "Eat pellets and avoid the ghosts.",
        "Power pellets let you chase ghosts briefly.",
        "",
        "Press any key to return",
    ])
    print(term.home + term.clear + term.bold_yellow(_center(text)))
    msvcrt.getch()
