"""Pac-Man domain entities."""

from dataclasses import dataclass


@dataclass
class Actor:
    x: int
    y: int
    direction: tuple[int, int] = (0, 0)
    next_direction: tuple[int, int] = (0, 0)


@dataclass
class Ghost:
    x: int
    y: int
    color: str
    direction: tuple[int, int] = (0, 0)
