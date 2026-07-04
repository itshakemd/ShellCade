"""Space Invaders entity types."""

from dataclasses import dataclass


@dataclass
class Projectile:
    x: int
    y: int
    dy: int
    owner: str


@dataclass
class Enemy:
    x: int
    y: int
    row: int
    alive: bool = True
