"""Live game loop for single-player and two-player matches."""

import os
import time

from constants import FRAME_DELAY
from input import read_keys


def run_game(game):
    while not game.match_over:
        keys = read_keys()
        if b"q" in keys or b"Q" in keys:
            return False
        if b"p" in keys or b"P" in keys:
            game.paused = not game.paused
        if not game.paused:
            if b"w" in keys or b"W" in keys:
                game.move_left(-1)
            if b"s" in keys or b"S" in keys:
                game.move_left(1)
            if game.two_player:
                if b"\x48" in keys:
                    game.move_right(-1)
                if b"\x50" in keys:
                    game.move_right(1)
            else:
                game.ai_move()
            game.tick()
        os.system("cls" if os.name == "nt" else "clear")
        print(game.render())
        time.sleep(FRAME_DELAY)
    return True
