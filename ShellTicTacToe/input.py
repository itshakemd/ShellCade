"""Non-blocking keyboard input."""

import msvcrt


def read_key() -> str | None:
    if not msvcrt.kbhit():
        return None
    return msvcrt.getwch().lower()
