"""Blocking keyboard input helpers built on msvcrt (Windows only)."""

import msvcrt

from constants import WIDTH
from display import clear_screen, print_centered


def read_key():
    """Blocking read of a single logical key press. Returns a short string code."""
    ch = msvcrt.getch()
    if ch in (b"\x00", b"\xe0"):
        ch2 = msvcrt.getch()
        if ch2 == b"H":
            return "UP"
        if ch2 == b"P":
            return "DOWN"
        if ch2 == b"K":
            return "LEFT"
        if ch2 == b"M":
            return "RIGHT"
        return ""
    if ch in (b"\r", b"\n"):
        return "ENTER"
    if ch in (b"w", b"W"):
        return "UP"
    if ch in (b"s", b"S"):
        return "DOWN"
    if ch in (b"a", b"A"):
        return "LEFT"
    if ch in (b"d", b"D"):
        return "RIGHT"
    if ch in (b"q", b"Q", b"\x1b"):
        return "ESC"
    return ""
