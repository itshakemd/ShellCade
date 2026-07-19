# ShellSpaceInvaders

ShellSpaceInvaders is a Windows terminal arcade shooter.

Install the root `requirements.txt` before playing to enable Blessed terminal
rendering.

The `ui.py` module isolates terminal styling from the simulation and collision
rules in `game.py`.

## Run

From this folder, run `python main.py` or launch `invaders.bat`.

## Controls

- `A` / `D` move the cannon
- `Space` fires
- `P` pauses or resumes
- `Q` returns to the menu

Destroy the descending invader formation, protect yourself with the shields,
and survive as many waves as possible.

Run the regression tests with:

```text
python -m unittest test_game.py
```
