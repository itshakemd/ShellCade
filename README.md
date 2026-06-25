# Shellsnake

Shellsnake is a terminal-based Snake game for Windows, built as part of the
Shellcade collection of classic arcade experiences.

## Features

- Real-time Snake gameplay in a terminal
- Arrow-key and WASD controls
- Pause, quit, and replay flow
- Persistent top-ten leaderboard
- Speed increases every 50 points
- No third-party Python dependencies

## Controls

| Key | Action |
| --- | --- |
| Arrow keys / W A S D | Steer the snake |
| P | Pause or resume |
| Q | Quit to the menu |
| Enter | Select a menu option |

Eat fruit to grow and earn 10 points. Avoid the walls and the snake's own
body. The game ends when the snake collides with an obstacle.

## How to Run

Open a Windows terminal in the project directory and run:

```text
python snake.py
```

You can also double-click `snake.bat`.

To run the rule regression tests:

```text
python -m unittest test_snake.py
```

## Project Structure

- `snake.py` - application entry point
- `game.py` - Snake state, collision rules, scoring, and rendering
- `game_loop.py` - real-time input and movement timing
- `menu.py` - menu, leaderboard, and instructions screens
- `display.py` - terminal rendering helpers
- `keyboard_input.py` - Windows keyboard and name-entry handling
- `scores.py` - persistent leaderboard storage
- `constants.py` - board dimensions and shared paths
- `test_snake.py` - regression tests for movement and collisions

## License

This project is intended for personal and educational use.
