"""Core game state and logic: board, scoring, line clears, rendering."""

from constants import WIDTH, HEIGHT, SHAPES
from piece import Piece, new_bag


class Game:
    def __init__(self):
        self.board = [[None] * WIDTH for _ in range(HEIGHT)]
        self.bag = new_bag()
        self.current = Piece(self.bag.pop())
        self.next_kind = self.bag.pop() if self.bag else None
        self.score = 0
        self.lines = 0
        self.level = 1
        self.game_over = False
        self.paused = False
        self.fall_time = 0.0

    def refill_bag_if_needed(self):
        if not self.bag:
            self.bag = new_bag()

    def valid(self, cells):
        for x, y in cells:
            if x < 0 or x >= WIDTH or y >= HEIGHT:
                return False
            if y >= 0 and self.board[y][x] is not None:
                return False
        return True

    def lock_piece(self):
