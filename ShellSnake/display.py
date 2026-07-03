"""Small terminal helpers: clearing the screen and centering text blocks."""

import os
import shutil


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def center_block(text, vertical=True):
    """Centers a multi-line block of text in the current terminal window.
    Each line is centered independently so that shorter/longer lines
    (e.g. the status line vs. the board) all sit symmetrically around
    the true horizontal center, rather than sharing one left margin."""
    cols, rows = shutil.get_terminal_size((80, 24))
    lines = text.split("\n")
    centered = []
    for line in lines:
        pad = max(0, (cols - len(line)) // 2)
        centered.append((" " * pad) + line)
    if vertical:
        vpad = max(0, (rows - len(centered)) // 2)
        centered = [""] * vpad + centered
    return "\n".join(centered)


def print_centered(text, vertical=True):
    print(center_block(text, vertical=vertical))
