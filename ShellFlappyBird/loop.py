"""Real-time Flappy Bird loop."""

import time

from constants import FRAME_DELAY
from input import read_keys
from ui import create_terminal, frame


def run_game(game):
    term = create_terminal()
    while not game.game_over:
        keys = read_keys()
        if b"q" in keys or b"Q" in keys:
            return False
        if b"p" in keys or b"P" in keys:
            game.paused = not game.paused
        if b" " in keys or b"\r" in keys:
            game.flap()
        game.tick()
        print(frame(term, game.render()))
        time.sleep(FRAME_DELAY)
    return True
