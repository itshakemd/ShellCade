"""Centered Tic-Tac-Toe menu."""

import msvcrt
import shutil


OPTIONS = ["Single Player", "Two Players", "Instructions", "Quit"]


def _center(text: str) -> str:
    columns, rows = shutil.get_terminal_size((80, 24))
    lines = text.splitlines()
    return "\n" * max(0, (rows - len(lines)) // 2) + "\n".join(line.center(columns) for line in lines)


def choose() -> str:
    selected = 0
    while True:
        lines = ["=" * 34, "SHELL TIC-TAC-TOE".center(34), "=" * 34, ""]
        lines += [(("> " if index == selected else "  ") + option).center(34)
                  for index, option in enumerate(OPTIONS)]
        lines += ["", "Use W/S or Up/Down, Enter to select"]
        print("\033[2J\033[H\033[33m" + _center("\n".join(lines)) + "\033[0m", end="")
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
    print("\033[2J\033[H" + _center(
        "TIC-TAC-TOE INSTRUCTIONS\n"
        "-----------------------\n"
        "Choose positions 1 through 9.\n"
        "Single Player: X versus the computer O.\n"
        "Two Players: alternate turns on one keyboard.\n"
        "R restarts after a round, Q returns to the menu.\n\n"
        "Press any key to return."
    ))
    msvcrt.getch()
