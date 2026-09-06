<div align="center">
<pre>
 _______   __                  __  __   _______                   __
 /      \ /  |                /  |/  | /      \                 /  |
$$$$$$  |$$ |____    ______  $$ |$$ |/$$$$$$  |  ______    ____$$ |  ______
$$ \__$$/ $$      \  /      \ $$ |$$ |$$ |  $$ | /      \  /    $$ | /      \
$$      \ $$$$$$$  |/$$$$$$  |$$ |$$ |$$ |       $$$$$$  |/$$$$$$$ |/$$$$$$  |
 $$$$$$  |$$ |  $$ |$$    $$ |$$ |$$ |$$ |   __  /    $$ |$$ |  $$ |$$    $$ |
/  __$$ |$$ |  $$ |$$$$$$$$/ $$ |$$ |$$ \__  |/$$$$$$$ |$$ \__$$ |$$$$$$$$/
$$    $$/ $$ |  $$ |$$       |$$ |$$ |$$    $$/ $$    $$ |$$    $$ |$$       |
 $$$$$$/  $$/   $$/  $$$$$$$/ $$/ $$/  $$$$$$/   $$$$$$$/  $$$$$$$/  $$$$$$$/
</pre>
</div>

# Shellcade

Shellcade is a collection of classic arcade games built for the Windows
terminal.

## Games

| Folder | Game | Run from the repository root |
| --- | --- | --- |
| `ShellSnake` | [Snake](#shellsnake) | `python ShellSnake/snake.py` |
| `ShellTetris` | [Tetris](#shelltetris) | `python ShellTetris/tetris.py` |
| `ShellPong` | [Pong](#shellpong) | `python ShellPong/main.py` |
| `ShellSpaceInvaders` | [Space Invaders](#shellspaceinvaders) | `python ShellSpaceInvaders/main.py` |
| `ShellFlappyBird` | [Flappy Bird](#shellflappybird) | `python ShellFlappyBird/main.py` |
| `ShellArkanoid` | [Arkanoid](#shellarkanoid) | `python -m ShellArkanoid.main` |
| `ShellPacman` | [Pac-Man](#shellpacman) | `python -m ShellPacman` |
| `ShellTicTacToe` | [Tic-Tac-Toe](#shelltictactoe) | `python -m ShellTicTacToe` |



Read the `README.md` inside a game folder for its controls, features, and
game-specific test command.

## Game Guide

### ShellSnake

#### Description

A real-time terminal Snake game with scoring, increasing
speed, replay support, and a persistent top-ten leaderboard.

#### Rules

Eat fruit to grow and earn 10 points. Avoid the walls and the
snake's own body. The game ends when the snake hits an obstacle.

#### Controls

Arrow keys or `W/A/S/D` steer the snake. `P` pauses or resumes,
`Q` returns to the menu, and `Enter` selects a menu option.

---

### ShellTetris

#### Description

A terminal Tetris game where falling pieces must be arranged
to clear complete rows.

#### Rules

Move and rotate each piece as it falls. Complete rows disappear and
score points; the falling speed increases as more rows are cleared. The game
ends when the pieces reach the top of the board.

#### Controls

`A/D` move, `S` soft-drops, `W` or Up rotates, and Space
hard-drops. `P` pauses and `Q` returns to the menu.

---

### ShellPong

#### Description

A terminal Pong game with single-player and two-player modes.

#### Rules

Return the ball with your paddle and score when your opponent
misses. The first player to reach seven points wins.

#### Controls

In single-player mode, Player 1 uses `W/S` and the computer
controls Player 2. In two-player mode, Player 1 uses `W/S` and Player 2 uses
Up/Down. `P` pauses and `Q` quits.

---

### ShellSpaceInvaders

#### Description

A terminal arcade shooter where a cannon battles descending
formations of invaders.

#### Rules

Destroy the invaders, use the shields for protection, and survive
as many waves as possible. The game ends when the invaders overrun the
defenses or the player is defeated.

#### Controls

`A/D` move the cannon, Space fires, `P` pauses or resumes, and
`Q` returns to the menu.

---

### ShellFlappyBird

#### Description

A terminal Flappy Bird game based on timing and vertical
movement through obstacles.

#### Rules

Flap through the gaps between pipes without crashing. The run ends
when the bird collides with an obstacle or the boundary.

#### Controls

Space or `Enter` flaps, `P` pauses or resumes, `R` restarts after
a crash, and `Q` returns to the menu.

---

### ShellArkanoid

#### Description

A terminal brick-breaking game with a paddle, bouncing ball,
colored bricks, and score-based progression.

#### Rules

Keep the ball in play and break the brick formation. Bricks in the
upper rows are worth more points; clearing the entire formation wins the
round.

#### Controls

`A/D` or the arrow keys move the paddle. `P` pauses, `R`
restarts after a round ends, and `Q` quits.

---

### ShellPacman

#### Description

A terminal Pac-Man game featuring pellets, power pellets,
and ghosts.

#### Rules

Eat pellets and power pellets while avoiding the ghosts. Pellets
are worth 10 points, power pellets are worth 50, and frightened ghosts are
worth 200 points.

#### Controls

Arrow keys or `W/A/S/D` move. `P` pauses, `R` restarts, and `Q`
returns to the menu.

---

### ShellTicTacToe

#### Description

A terminal Tic-Tac-Toe game against a simple computer
opponent or another person at the same keyboard.

#### Rules

Players take turns placing their marks on a 3x3 board. Complete a
row, column, or diagonal with three matching marks to win; if the board fills
without a winner, the game is a draw.

#### Controls

Choose a mode with `W/S` or Up/Down and `Enter`. During a match,
select board positions with keys `1` through `9`. `R` restarts and `Q` returns
to the menu.

## Setup

Use Python 3 on Windows. From the repository root, install the only external
dependency:

```powershell
python -m pip install -r requirements.txt
```

Then run any game from the table above. A terminal window large enough for the
game board is recommended.

## Tests

Each game includes focused tests. For package-based games, run the test module
from the repository root, for example:

```powershell
python -m unittest ShellTicTacToe.test_game
```



