"""Non-blocking Windows keyboard input."""

import msvcrt


def read_keys():
    keys = set()
    while msvcrt.kbhit():
        keys.add(msvcrt.getch())
    return keys
