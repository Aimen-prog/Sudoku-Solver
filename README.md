
Soduku Solver
======

**About this repository**
<br>
Sudoku Solver using backtracking and brute forcing - LaPlateforme Formation 
<hr>
Backtracking approach: 
        Starts by finding the first empty cell in the grid and tries to place numbers
        from 1 to 9 in that cell while checking if the placement is valid according to
        Sudoku rules (no duplicates in the same row, column, or 3x3 subgrid). If a valid
        placement is found, the method recursively attempts to solve the remaining puzzle.

<br>
Brute Force approach:
        Iterates through the Sudoku grid, attempting to place numbers from 1 to 9
        at empty cells while checking if the placement is valid. If a valid placement is found,
        it continues solving the puzzle recursively.
<hr>

**Get started**

using the terminal:

```bash
cd ~/Sudoku-Solver
python3 main.py

```

A more user-friendly way:

```bash
cd ~/Sudoku-Solver
python3 pygame_soduku.py

```

Benchmarking: The goal here is to compare the execution time of (1) brute force vs (2) backtracking method on 5 files
that can be found in the 'soduku_puzzles' folder (Average execution time of these files).

```bash
cd ~/Sudoku-Solver
python3 benchmarking.py

```

=> The backtracking method is better because it takes less time compared to the naive resolution of the brute forcing 

# Author
Aimen CHERIF