# DFS Tic Tac Toe

## Introduction
This project implements the Depth-First Search (DFS) algorithm in a simple tic-tac-toe game. The game pits a human player against a computer opponent that uses the minimax strategy to determine its moves.

## Gameplay Description
- The player (X) starts the game.
- The computer (O) navigates all possible plays to determine the best possible move using the minimax function. This function iterates through all possible outcomes and selects the move that minimizes the potential gain of the opponent, assuming the opponent plays optimally.
- If the player makes a suboptimal move, the computer adjusts its strategy to exploit this, potentially leading to a quicker victory for the computer.

## How to Play
1. Run the game script in a Python environment.
2. Enter the row and column where you wish to place your 'X'. Rows and columns are numbered 1 through 3.
3. The computer will automatically calculate and make its move after each player turn.
4. The game continues until one player wins or all spaces are filled, resulting in a draw.

## Features
- **Intelligent Computer Opponent**: Utilizes a depth-first search algorithm combined with minimax logic to simulate a challenging opponent.
- **Simple Console Interface**: Game play occurs in the command line, where players input their moves and view the game board.

## How to Run
Ensure you have Python installed on your machine. Then, clone this repository and run the game script:

```bash
python tic_tac_toe.py
```

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

As for your script, make sure it's well-commented, and consider adding error handling or user input validation where necessary. You might also add more in-depth comments explaining how the minimax function and DFS are implemented and work within the context of the game to help others understand the code better.

Including a license is generally a good practice, as previously discussed, and you can follow the steps provided in the previous response to include a license like MIT, which is common and permissive for such projects.
