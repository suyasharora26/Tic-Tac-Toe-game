# Tic-Tac-Toe Game

This is a simple two-player Tic-Tac-Toe game made with Python. Players take turns entering a number from 1 to 9 to place an `X` or an `O` on the board.

## Requirements

- Python 3

## How to Run

Open a terminal in this folder and run:

```bash
python3 tictactoe_revised.py
```

## How to Play

The board positions are numbered from left to right, top to bottom:

```text
1 | 2 | 3
--+---+--
4 | 5 | 6
--+---+--
7 | 8 | 9
```

- Player X goes first.
- Enter a number between 1 and 9 when asked.
- A position cannot be used more than once.
- The first player to get three matching marks in a row, column, or diagonal wins.
- If every position is filled and nobody wins, the game ends in a draw.

## Code Overview

- `show_board()` prints the current game board.
- `check_winner()` checks all possible winning lines.
- `is_board_full()` checks whether there are any empty positions left.
- The main loop gets each player's move, validates it, and changes turns.
