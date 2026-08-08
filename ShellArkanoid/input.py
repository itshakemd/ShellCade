"""Windows-friendly non-blocking keyboard input."""

import msvcrt


ARROW_KEYS = {"K": "left", "M": "right"}


def read_key() -> str | None:
    if not msvcrt.kbhit():
        return None
    key = msvcrt.getwch()
    if key in ("\x00", "\xe0"):
        return ARROW_KEYS.get(msvcrt.getwch(), None) if msvcrt.kbhit() else None
    return key.lower()
