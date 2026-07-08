"""Live Space Invaders loop."""

import os
import time

from constants import FRAME_DELAY
from input import read_keys


def run_game(game):
    while not game.game_over:
        keys = read_keys()
        if b"q" in keys or b"Q" in keys:
            return False
        if b"p" in keys or b"P" in keys:
            game.paused = not game.paused
        if not game.paused:
            if b"a" in keys or b"A" in keys:
                game.move_player(-2)
            if b"d" in keys or b"D" in keys:
                game.move_player(2)
            if b" " in keys:
                game.fire()
            game.tick()
        os.system("cls" if os.name == "nt" else "clear")
        print(game.render())
        time.sleep(FRAME_DELAY)
    return True
