"""Non-blocking Windows keyboard input."""

import msvcrt


def read_key() -> str | None:
    if not msvcrt.kbhit():
        return None
    key = msvcrt.getwch()
    if key in ("\x00", "\xe0") and msvcrt.kbhit():
        return {"H": "up", "P": "down", "K": "left", "M": "right"}.get(msvcrt.getwch())
    return key.lower()
