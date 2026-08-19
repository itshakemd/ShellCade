"""Non-blocking Windows keyboard input."""

import msvcrt


ARROW_KEYS = {"H": "up", "P": "down", "K": "left", "M": "right"}


def read_key() -> str | None:
    if not msvcrt.kbhit():
        return None
    key = msvcrt.getwch()
    if key in ("\x00", "\xe0") and msvcrt.kbhit():
        return ARROW_KEYS.get(msvcrt.getwch())
    return key.lower()
