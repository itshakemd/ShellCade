"""Single-player Tic-Tac-Toe opponent."""

from .game import TicTacToeGame


def choose_move(game: TicTacToeGame) -> int:
    for move in game.available_moves():
        trial = TicTacToeGame()
        trial.board = game.board.copy()
        trial.current = "O"
        trial.play(move)
        if trial.winner == "O":
            return move
    if 4 in game.available_moves():
        return 4
    return game.available_moves()[0]
