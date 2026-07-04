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

Shellcade is a collection of classic arcade games implemented for the Windows
terminal. Each game is self-contained in its own folder.

## Games

| Folder | Game | Run |
| --- | --- | --- |
| `ShellSnake` | Snake | `python snake.py` |
| `ShellTetris` | Tetris | `python tetris.py` |
| `ShellPong` | Pong | `python main.py` |

Open a game folder before running its command. Windows users can also launch
the matching `.bat` file where provided.

Each folder contains its own game logic, display helpers, controls, and score
data so the games can evolve independently.
