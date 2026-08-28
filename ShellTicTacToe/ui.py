"""Blessed Tic-Tac-Toe presentation."""

import shutil

from blessed import Terminal


class TicTacToeUI:
    def __init__(self, term: Terminal) -> None:
        self.term = term

    @staticmethod
    def position_label(index: int) -> str:
        return str(index + 1)

    @staticmethod
    def center_block(text: str, columns: int, rows: int) -> str:
        lines = text.splitlines()
        width = max((len(line) for line in lines), default=0)
        left_padding = max(0, (columns - width) // 2)
        top_padding = max(0, (rows - len(lines)) // 2)
        return "\n" * top_padding + "\n".join(
            " " * left_padding + line.center(width) for line in lines
        )

    def draw(self, game, single_player: bool) -> str:
        lines = ["TIC-TAC-TOE", f"Mode: {'Single Player' if single_player else 'Two Players'}",
                 f"Turn: {game.current}", ""]
        for row in range(3):
            cells = [
                game.board[row * 3 + column] if game.board[row * 3 + column] != " "
                else self.position_label(row * 3 + column)
                for column in range(3)
            ]
            lines.append(f" {cells[0]} | {cells[1]} | {cells[2]} ")
            if row < 2:
                lines.append("---+---+---")
        if game.winner:
            lines.extend(["", f"Player {game.winner} wins!", "Press R to play again or Q to quit"])
        elif game.draw:
            lines.extend(["", "Draw game!", "Press R to play again or Q to quit"])
        else:
            lines.extend(["", "Choose a position with 1-9", "Q quits"])
        columns, rows = shutil.get_terminal_size((80, 24))
        return self.center_block("\n".join(lines), columns, rows)
