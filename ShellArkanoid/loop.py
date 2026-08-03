"""Real-time terminal loop for Arkanoid."""

import time

from blessed import Terminal

from .constants import TICK_SECONDS
from .game import ArkanoidGame
from .input import read_key
from .ui import ArkanoidUI


def run_game(term: Terminal) -> ArkanoidGame:
    game = ArkanoidGame()
    ui = ArkanoidUI(term)
    with term.fullscreen(), term.cbreak(), term.hidden_cursor():
        while True:
            key = read_key()
            if key in ("q", "\x03"):
                break
            if key in ("a", "h", "KEY_LEFT"):
                game.move_paddle(-2)
            elif key in ("d", "l", "KEY_RIGHT"):
                game.move_paddle(2)
            elif key == "p":
                game.toggle_pause()
            elif key == "r" and game.game_over:
                game = ArkanoidGame()
            game.tick()
            print(term.home + term.clear + ui.draw(game), end="", flush=True)
            time.sleep(TICK_SECONDS)
    return game
