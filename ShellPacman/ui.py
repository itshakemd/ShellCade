"""Blessed Pac-Man board renderer."""

import shutil

from blessed import Terminal

from .constants import BOARD, HEIGHT, WIDTH
from .game import PacmanGame


class PacmanUI:
    def __init__(self, term: Terminal) -> None:
        self.term = term

    def _actor_at(self, game: PacmanGame, x: int, y: int):
        return next((ghost for ghost in game.ghosts if (ghost.x, ghost.y) == (x, y)), None)

    @staticmethod
    def _center_block(text: str, columns: int, rows: int) -> str:
        lines = text.splitlines()
        left_padding = max(0, (columns - WIDTH) // 2)
        top_padding = max(0, (rows - len(lines)) // 2)
        return "\n" * top_padding + "\n".join(
            " " * left_padding + line for line in lines
        )

    def draw(self, game: PacmanGame) -> str:
        lines = [f" SCORE {game.score:05d}   LIVES {game.lives}   DOTS {game.remaining_collectibles:03d}"]
        for y in range(HEIGHT):
            row = []
            for x in range(WIDTH):
                if (x, y) == (game.pacman.x, game.pacman.y):
                    row.append(self.term.bold_yellow + "C" + self.term.normal)
                elif (ghost := self._actor_at(game, x, y)):
                    style = getattr(self.term, "bold_" + ghost.color, self.term.bold_red)
                    row.append(style + ("g" if game.frightened_ticks else "G") + self.term.normal)
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
        columns, rows = shutil.get_terminal_size((80, 24))
        return self._center_block("\n".join(lines), columns, rows)
