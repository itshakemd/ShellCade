"""The falling piece and the 7-bag randomizer."""

from constants import SHAPES


class Piece:
    def __init__(self, kind):
        self.kind = kind
        self.rot = 0
        self.x = 3
        self.y = 0

    def cells(self, rot=None, x=None, y=None):
        rot = self.rot if rot is None else rot
        x = self.x if x is None else x
        y = self.y if y is None else y
        states = SHAPES[self.kind]
        shape = states[rot % len(states)]
        return [(x + cx, y + cy) for cx, cy in shape]
