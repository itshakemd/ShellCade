# ShellTetris

ShellTetris is the original terminal Tetris game in the Shellcade collection.

Install the root `requirements.txt` before playing to enable Blessed terminal
rendering.

Terminal lifecycle and frame styling live in `ui.py`; board rules remain in
`game.py` for easier testing and maintenance.

## Run

From this folder, run `python tetris.py` or double-click `tetris.bat`.

## Controls

- `A` / `D` move the piece
- `S` soft-drops
- `W` or Up rotates
- Space hard-drops
- `P` pauses and `Q` returns to the menu

Clear lines to score points. The falling speed increases as more lines are
cleared.
