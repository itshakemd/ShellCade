"""Blessed Pac-Man board renderer."""

from blessed import Terminal

from .constants import BOARD, HEIGHT, WIDTH
from .game import PacmanGame


class PacmanUI:
    def __init__(self, term: Terminal) -> None:
        self.term = term

    def draw(self, game: PacmanGame) -> str:
        lines = [f" SCORE {game.score:05d}   LIVES {game.lives}   DOTS {game.remaining_collectibles:03d}"]
        for y in range(HEIGHT):
            row = []
            for x in range(WIDTH):
                if (x, y) == (game.pacman.x, game.pacman.y):
                    row.append(self.term.bold_yellow + "C" + self.term.normal)
                elif any((ghost.x, ghost.y) == (x, y) for ghost in game.ghosts):
                    row.append(self.term.bold_red + "G" + self.term.normal)
                elif (x, y) in game.power_pellets:
                    row.append(self.term.bold_white + "o" + self.term.normal)
                elif (x, y) in game.pellets:
                    row.append(self.term.yellow + "." + self.term.normal)
                else:
                    row.append(self.term.blue + ("#" if BOARD[y][x] == "#" else " ") + self.term.normal)
            lines.append("".join(row))
        if game.paused:
            lines.append("PAUSED - press P to resume")
        elif game.game_over:
            lines.append("YOU WIN!" if game.won else "GAME OVER - press R to restart")
        return "\n".join(lines)
