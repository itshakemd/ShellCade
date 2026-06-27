"""Windows non-blocking keyboard input for ShellPong."""

import msvcrt


def read_keys():
    keys = set()
    while msvcrt.kbhit():
        key = msvcrt.getch()
        if key in (b"\x00", b"\xe0"):
            key = msvcrt.getch()
        keys.add(key)
    return keys
