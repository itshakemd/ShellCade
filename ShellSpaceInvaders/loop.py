"""Live Space Invaders loop."""

import time

from constants import FRAME_DELAY
from input import read_keys
from ui import create_terminal, terminal_frame


def run_game(game):
    term = create_terminal()
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
        print(terminal_frame(term, game.render()))
        time.sleep(FRAME_DELAY)
    return True
