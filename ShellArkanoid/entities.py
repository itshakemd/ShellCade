"""Arkanoid value objects."""

from dataclasses import dataclass


@dataclass
class Paddle:
    x: int
    width: int

    @property
    def right(self) -> int:
        return self.x + self.width - 1


@dataclass
class Ball:
    x: int
    y: int
    dx: int = 1
    dy: int = -1


@dataclass
class Brick:
    x: int
    y: int
    width: int
    row: int
    alive: bool = True
