"""Deterministic Pac-Man game rules."""

from __future__ import annotations

from .constants import (
    BOARD,
    GHOST_STARTS,
    HEIGHT,
    PELLET_SCORE,
    STARTING_LIVES,
    START_X,
    START_Y,
    WIDTH,
)
from .entities import Actor, Ghost


class PacmanGame:
    def __init__(self) -> None:
        self.pacman = Actor(START_X, START_Y)
        colors = ("red", "pink", "cyan", "orange")
        self.ghosts = [Ghost(x, y, color) for (x, y), color in zip(GHOST_STARTS, colors)]
        self.pellets = {
            (x, y)
            for y, row in enumerate(BOARD)
            for x, cell in enumerate(row)
            if cell == "."
        }
        self.score = 0
        self.lives = STARTING_LIVES
        self.paused = False
        self.game_over = False
        self.won = False

    def is_wall(self, x: int, y: int) -> bool:
        return not (0 <= x < WIDTH and 0 <= y < HEIGHT) or BOARD[y][x] == "#"

    def set_direction(self, direction: tuple[int, int]) -> None:
        if not self.game_over:
            self.pacman.next_direction = direction

    def tick(self) -> None:
        if self.paused or self.game_over:
            return
        if not self.is_wall(self.pacman.x + self.pacman.next_direction[0], self.pacman.y + self.pacman.next_direction[1]):
            self.pacman.direction = self.pacman.next_direction
        nx = self.pacman.x + self.pacman.direction[0]
        ny = self.pacman.y + self.pacman.direction[1]
        if not self.is_wall(nx, ny):
            self.pacman.x, self.pacman.y = nx, ny
        if (self.pacman.x, self.pacman.y) in self.pellets:
            self.pellets.remove((self.pacman.x, self.pacman.y))
            self.score += PELLET_SCORE
        if not self.pellets:
            self.won = True
            self.game_over = True
        self._move_ghosts()
        self._check_collisions()

    def toggle_pause(self) -> None:
        if not self.game_over:
            self.paused = not self.paused

    def restart(self) -> None:
        self.__init__()
