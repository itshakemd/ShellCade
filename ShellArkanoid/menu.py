"""Centered, keyboard-navigable Arkanoid menu."""

import msvcrt
import shutil

from blessed import Terminal


OPTIONS = ["Play", "Instructions", "Quit"]


def _center(text: str) -> str:
    columns, rows = shutil.get_terminal_size((80, 24))
    lines = text.splitlines()
    top_padding = max(0, (rows - len(lines)) // 2)
    return "\n" * top_padding + "\n".join(line.center(columns) for line in lines)


def _read_menu_key() -> str:
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


def _draw_menu(selected: int) -> str:
    width = 34
    lines = [
        "=" * width,
        "SHELL ARKANOID".center(width),
        "=" * width,
        "",
    ]
    lines.extend(
        (("> " if index == selected else "  ") + option).center(width)
        for index, option in enumerate(OPTIONS)
    )
    lines.extend(["", "Use W/S or Up/Down, Enter to select".center(width)])
    return "\n".join(lines)


def choose() -> str:
    term = Terminal()
    selected = 0
    while True:
        print(term.home + term.clear + term.bold_yellow(_center(_draw_menu(selected))))
        key = _read_menu_key()
        if key == "UP":
            selected = (selected - 1) % len(OPTIONS)
        elif key == "DOWN":
            selected = (selected + 1) % len(OPTIONS)
        elif key == "ENTER":
            return OPTIONS[selected]
        elif key == "QUIT":
            return "Quit"


def show_instructions() -> None:
    term = Terminal()
    text = "\n".join([
        "SHELL ARKANOID INSTRUCTIONS",
        "-" * 34,
        "A / D or arrows  move the paddle",
        "P                pause / resume",
        "R                restart after a round",
        "Q                quit to the menu",
        "",
        "Clear all bricks to win.",
        "Upper rows are worth more points.",
        "",
        "Press any key to return",
    ])
    print(term.home + term.clear + term.bold_yellow(_center(text)))
    msvcrt.getch()
