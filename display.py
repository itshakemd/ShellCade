"""Small terminal helpers: clearing the screen and centering text blocks."""

import os


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")
