"""The falling piece and the 7-bag randomizer."""

from constants import SHAPES


class Piece:
    def __init__(self, kind):
        self.kind = kind
        self.rot = 0
        self.x = 3
        self.y = 0
