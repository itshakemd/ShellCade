"""Real-time Pac-Man loop."""

import time

from blessed import Terminal

from .constants import TICK_SECONDS
from .game import PacmanGame
from .input import read_key
from .ui import PacmanUI


DIRECTIONS = {"up": (0, -1), "down": (0, 1), "left": (-1, 0), "right": (1, 0)}


def run_game(term: Terminal) -> PacmanGame:
    game = PacmanGame()
    ui = PacmanUI(term)
    with term.fullscreen(), term.cbreak(), term.hidden_cursor():
        while True:
            key = read_key()
            while key is not None:
                if key in ("q", "\x03"):
                    return game
                if key in DIRECTIONS:
                    game.set_direction(DIRECTIONS[key])
                elif key == "p":
                    game.toggle_pause()
                elif key == "r" and game.game_over:
                    game.restart()
                key = read_key()
            game.tick()
            print(term.home + term.clear + ui.draw(game), end="", flush=True)
            time.sleep(TICK_SECONDS)
