"""Blessed Tic-Tac-Toe presentation."""

from blessed import Terminal


class TicTacToeUI:
    def __init__(self, term: Terminal) -> None:
        self.term = term

    def draw(self, game, single_player: bool) -> str:
        lines = ["TIC-TAC-TOE", f"Mode: {'Single Player' if single_player else 'Two Players'}",
                 f"Turn: {game.current}", ""]
        for row in range(3):
            cells = [game.board[row * 3 + column] for column in range(3)]
            lines.append(f" {cells[0]} | {cells[1]} | {cells[2]} ")
            if row < 2:
                lines.append("---+---+---")
        if game.winner:
            lines.extend(["", f"Player {game.winner} wins!", "Press R to play again or Q to quit"])
        elif game.draw:
            lines.extend(["", "Draw game!", "Press R to play again or Q to quit"])
        else:
            lines.extend(["", "Choose a position with 1-9", "Q quits"])
        return "\n".join(lines)
