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
        for x, y in self.current.cells():
            if y < 0:
                self.game_over = True
                return
            self.board[y][x] = self.current.kind
        self.clear_lines()
        self.spawn_next()

    def spawn_next(self):
        self.refill_bag_if_needed()
        kind = self.next_kind if self.next_kind else self.bag.pop()
        self.refill_bag_if_needed()
        self.next_kind = self.bag.pop()
        self.current = Piece(kind)
        if not self.valid(self.current.cells()):
            self.game_over = True

    def clear_lines(self):
        new_board = [row for row in self.board if any(c is None for c in row)]
        cleared = HEIGHT - len(new_board)
        for _ in range(cleared):
            new_board.insert(0, [None] * WIDTH)
        self.board = new_board
        if cleared:
            points = {1: 100, 2: 300, 3: 500, 4: 800}
            self.score += points.get(cleared, 0) * self.level
            self.lines += cleared
            self.level = 1 + self.lines // 10

    def move(self, dx, dy):
        cells = self.current.cells(x=self.current.x + dx, y=self.current.y + dy)
        if self.valid(cells):
            self.current.x += dx
            self.current.y += dy
            return True
        return False

    def clear_lines(self):
        new_board = [row for row in self.board if any(c is None for c in row)]
        cleared = HEIGHT - len(new_board)
        for _ in range(cleared):
            new_board.insert(0, [None] * WIDTH)
        self.board = new_board
        if cleared:
            points = {1: 100, 2: 300, 3: 500, 4: 800}
            self.score += points.get(cleared, 0) * self.level
            self.lines += cleared
            self.level = 1 + self.lines // 10

    def rotate(self):
        states = len(SHAPES[self.current.kind])
        new_rot = (self.current.rot + 1) % states
        cells = self.current.cells(rot=new_rot)
        if self.valid(cells):
            self.current.rot = new_rot
            return
        # simple wall kicks
        for dx in (-1, 1, -2, 2):
            kicked = self.current.cells(rot=new_rot, x=self.current.x + dx)
            if self.valid(kicked):
                self.current.rot = new_rot
                self.current.x += dx
                return
