"""Blessed presentation for Arkanoid."""

from blessed import Terminal

from .constants import BOARD_HEIGHT, BOARD_WIDTH, PADDLE_ROW
from .game import ArkanoidGame


class ArkanoidUI:
    def __init__(self, term: Terminal) -> None:
        self.term = term

    def draw(self, game: ArkanoidGame) -> str:
        lines = [f" SCORE {game.score:05d}   LIVES {game.lives}   BRICKS {game.remaining_bricks:02d}"]
        lines.append("+" + "-" * BOARD_WIDTH + "+")
        brick_map = {(brick.x, brick.y): brick for brick in game.bricks if brick.alive}
        for y in range(BOARD_HEIGHT):
            row = []
            for x in range(BOARD_WIDTH):
                if (x, y) in brick_map:
                    row.append(self.term.on_color(4) + " " + self.term.normal)
                elif y == PADDLE_ROW and game.paddle.x <= x <= game.paddle.right:
                    row.append(self.term.bold_cyan + "=" + self.term.normal)
                elif (x, y) == (game.ball.x, game.ball.y):
                    row.append(self.term.bold_yellow + "o" + self.term.normal)
                else:
                    row.append(" ")
            lines.append("|" + "".join(row) + "|")
        lines.append("+" + "-" * BOARD_WIDTH + "+")
        if game.paused:
            lines.append(" PAUSED - press P to resume")
        elif game.game_over:
            lines.append(" YOU WIN! " if game.won else " GAME OVER ")
        return "\n".join(lines)
