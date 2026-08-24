"""Tic-Tac-Toe gameplay loop."""

import time

from blessed import Terminal

from .ai import choose_move
from .game import TicTacToeGame
from .input import read_key
from .ui import TicTacToeUI


def run_game(term: Terminal, single_player: bool) -> None:
    game = TicTacToeGame()
    ui = TicTacToeUI(term)
    with term.fullscreen(), term.cbreak(), term.hidden_cursor():
        while True:
            key = read_key()
            if key == "q":
                return
            if key == "r" and game.finished:
                game = TicTacToeGame()
            elif key and key in "123456789" and not game.finished:
                game.play(int(key) - 1)
            if single_player and game.current == "O" and not game.finished:
                game.play(choose_move(game))
            print(term.home + term.clear + term.center(ui.draw(game, single_player)), end="", flush=True)
            time.sleep(0.05)
