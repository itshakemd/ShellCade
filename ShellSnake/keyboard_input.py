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


def get_text_input(prompt, max_len=12):
    """Reads a line of text via msvcrt, letting the user type and backspace.
    Returns the typed text (or a placeholder if left empty)."""
    text = ""
    width = WIDTH * 2 + 2
    while True:
        clear_screen()
        block = "\n".join([
            "=" * width,
            prompt.center(width),
            "=" * width,
            "",
            (text + "_").center(width),
            "",
            "Type your name, Enter to confirm".center(width),
        ])
        print_centered(block)

        ch = msvcrt.getch()
        if ch in (b"\r", b"\n"):
            return text.strip() or "Player"
        elif ch == b"\x08":  # backspace
            text = text[:-1]
        elif ch in (b"\x00", b"\xe0"):
            msvcrt.getch()  # swallow special-key second byte
        else:
            try:
                decoded = ch.decode("ascii")
            except UnicodeDecodeError:
                continue
            if decoded.isprintable() and len(text) < max_len:
                text += decoded
