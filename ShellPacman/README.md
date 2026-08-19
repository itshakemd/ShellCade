# Shell Pac-Man

Eat pellets, collect power pellets, and avoid the ghosts in this Blessed
terminal Pac-Man game.

## Run

```text
python -m ShellPacman
```

Windows users can double-click `pacman.bat`.

## Controls

Use the arrow keys or `W/A/S/D` to move. Press `P` to pause, `R` to restart,
and `Q` to return to the menu.

## Tests

```text
python -m unittest ShellPacman.test_game
```

Pellets are worth 10 points, power pellets are worth 50, and frightened ghosts
are worth 200.
