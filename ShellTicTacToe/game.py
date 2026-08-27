"""Tic-Tac-Toe rules and match state."""

from __future__ import annotations

from .constants import STARTING_PLAYER


class TicTacToeGame:
    def __init__(self) -> None:
        self.board = [" "] * 9
        self.current = STARTING_PLAYER
        self.winner: str | None = None
        self.draw = False

    @property
    def finished(self) -> bool:
        return self.winner is not None or self.draw

    def play(self, position: int) -> bool:
        if self.finished or not 0 <= position < 9 or self.board[position] != " ":
            return False
        self.board[position] = self.current
        if self._has_won(self.current):
            self.winner = self.current
        elif " " not in self.board:
            self.draw = True
        else:
            self.current = "O" if self.current == "X" else "X"
        return True

    def _has_won(self, mark: str) -> bool:
        lines = ((0, 1, 2), (3, 4, 5), (6, 7, 8),
                 (0, 3, 6), (1, 4, 7), (2, 5, 8),
                 (0, 4, 8), (2, 4, 6))
        return any(all(self.board[index] == mark for index in line) for line in lines)

    def available_moves(self) -> list[int]:
        return [index for index, value in enumerate(self.board) if value == " "]

    def reset(self) -> None:
        self.__init__()
