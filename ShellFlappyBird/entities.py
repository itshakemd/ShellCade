"""Flappy Bird value objects."""

from dataclasses import dataclass


@dataclass
class Bird:
    x: int
    y: float
    velocity: float = 0.0


@dataclass
class Pipe:
    x: float
    gap_y: int
    scored: bool = False
