"""Deterministic Arkanoid rules and state transitions."""

from __future__ import annotations

from .constants import (
    BALL_START_X,
    BALL_START_Y,
    BOARD_HEIGHT,
    BOARD_WIDTH,
    BRICK_COLUMNS,
    BRICK_GAP,
    BRICK_ROWS,
    BRICK_TOP,
    BRICK_WIDTH,
    PADDLE_ROW,
    PADDLE_WIDTH,
    STARTING_LIVES,
)
from .entities import Ball, Brick, Paddle


class ArkanoidGame:
    def __init__(self) -> None:
        self.paddle = Paddle((BOARD_WIDTH - PADDLE_WIDTH) // 2, PADDLE_WIDTH)
        self.ball = Ball(BALL_START_X, BALL_START_Y)
        self.bricks = self._build_bricks()
        self.score = 0
        self.lives = STARTING_LIVES
        self.paused = False
        self.game_over = False
        self.won = False

    @property
    def remaining_bricks(self) -> int:
        return sum(brick.alive for brick in self.bricks)

    @staticmethod
    def _build_bricks() -> list[Brick]:
        bricks = []
        total_width = BRICK_COLUMNS * BRICK_WIDTH + (BRICK_COLUMNS - 1) * BRICK_GAP
        left = (BOARD_WIDTH - total_width) // 2
        for row in range(BRICK_ROWS):
            for column in range(BRICK_COLUMNS):
                bricks.append(
                    Brick(
                        left + column * (BRICK_WIDTH + BRICK_GAP),
                        BRICK_TOP + row,
                        BRICK_WIDTH,
                        row,
                    )
                )
        return bricks

    def move_paddle(self, direction: int) -> None:
        if self.game_over:
            return
        self.paddle.x = max(0, min(BOARD_WIDTH - self.paddle.width, self.paddle.x + direction))

    def toggle_pause(self) -> None:
        if not self.game_over:
            self.paused = not self.paused

    def restart(self) -> None:
        self.__init__()

    def tick(self) -> None:
        if self.paused or self.game_over:
            return
        next_x = self.ball.x + self.ball.dx
        next_y = self.ball.y + self.ball.dy
        if next_x < 0 or next_x >= BOARD_WIDTH:
            self.ball.dx *= -1
            next_x = self.ball.x + self.ball.dx
        if next_y < 0:
            self.ball.dy = 1
            next_y = self.ball.y + self.ball.dy
        self.ball.x, self.ball.y = next_x, next_y
        self._resolve_bricks()
        self._resolve_paddle()
        if self.ball.y >= BOARD_HEIGHT:
            self._lose_ball()

    def _resolve_bricks(self) -> None:
        for brick in self.bricks:
            if brick.alive and brick.x <= self.ball.x < brick.x + brick.width and brick.y == self.ball.y:
                brick.alive = False
                self.ball.dy *= -1
                self.score += (BRICK_ROWS - brick.row) * 10
                if not any(item.alive for item in self.bricks):
                    self.won = True
                    self.game_over = True
                return

    def _resolve_paddle(self) -> None:
        if self.ball.dy > 0 and self.ball.y == PADDLE_ROW - 1:
            if self.paddle.x <= self.ball.x <= self.paddle.right:
                self.ball.dy = -1
                offset = self.ball.x - self.paddle.x
                self.ball.dx = -1 if offset < self.paddle.width // 3 else 1 if offset > self.paddle.width * 2 // 3 else self.ball.dx

    def _lose_ball(self) -> None:
        self.lives -= 1
        if self.lives <= 0:
            self.game_over = True
            return
        self.ball = Ball(BALL_START_X, BALL_START_Y)
