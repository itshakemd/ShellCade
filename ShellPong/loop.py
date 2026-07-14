"""Live game loop for single-player and two-player matches."""

import time

from blessed import Terminal

from constants import FRAME_DELAY
from input import DOWN, UP, read_keys


def run_game(game):
    term = Terminal()
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
                if UP in keys:
                    game.move_right(-1)
                if DOWN in keys:
                    game.move_right(1)
            else:
                game.ai_move()
            game.tick()
        print(term.home + term.clear + term.bold_yellow(game.render()))
        time.sleep(FRAME_DELAY)
    return True
