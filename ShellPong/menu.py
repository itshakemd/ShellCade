"""Text menu for selecting a ShellPong mode."""

import msvcrt


def choose_mode():
    print("SHELLPONG")
    print("==========")
    print("1. Single player")
    print("2. Two players")
    print("Q. Quit")
    while True:
        key = msvcrt.getch().lower()
        if key == b"1":
            return False
        if key == b"2":
            return True
        if key == b"q":
            return None
