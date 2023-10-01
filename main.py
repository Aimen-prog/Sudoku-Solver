import os
import numpy as np
from backtracking import Backtracking
from bruteForce import BruteForce


def file_holder(file_name):
    """
    Read a text file, clean its contents, and convert it into a 9x9 NumPy array of integers.

    Parameters:
    - file_name (str): The name of the text file to read.

    Returns:
    - numpy.ndarray: A 9x9 NumPy array containing the cleaned and converted data from the file.
    """
    with open(file_name, 'r') as f:
        file = f.read()
    file = file.replace(' ', '').replace('\n', '').replace('_', "0")
    return (np.array(list(file)).astype(int)).reshape((9, 9))


def get_coordinates(grid):
    """
    Get the coordinates of non-zero elements in a 2D grid.

    Parameters:
    - grid (list of lists): The 2D grid to analyze.

    Returns:
    - list of tuples: A list of tuples containing the (row, column) coordinates
      of non-zero elements in the grid.
    """
    coordinates = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] > 0:
                coordinates.append((i, j))
    return coordinates


def print_grid(grid, coordinates):
    """
    Print a 9x9 Sudoku grid with highlighted coordinates.

    Parameters:
    - grid (list of lists): The 9x9 Sudoku grid to print.
    - coordinates (list of tuples): A list of (row, column) coordinates to highlight.

    Returns:
    - str: The final horizontal separator line for the grid.
    """
    hsep = "\033[34m" + " _______________________" + "\033[0m"
    vsep = "\033[34m" + "|" + "\033[0m"
    print(hsep)
    for i in range(len(grid)):
        print(vsep, end=" ")
        for j in range(len(grid[i])):
            current = str(grid[i][j])
            if (i, j) in coordinates:
                current = f"\033[32m{current}\033[0m"  # Set text color to green
            if j % 3 == 0 and j != 0:
                print(vsep, end=" ")
            print(current, end=" ")
        print(vsep, end=" ")
        print("")
        if i != 8 and i % 3 == 2:
            print(hsep)
    return hsep


def execute():
    """
    Run a Sudoku solver program with user interaction.

    This function prompts the user to enter the name of a valid Sudoku puzzle file (.txt).
    It then reads the puzzle from the file, allows the user to choose between Brute Force
    and Backtracking solvers, and attempts to solve the Sudoku puzzle using the selected
    solver. If a solution is found, it displays the solved Sudoku grid.
    The user can choose to solve another puzzle or exit the program.

    The function runs in a loop until the user decides to exit.
    """
    while True:
        file_name = input("Please enter a valid file (.txt): ")
        if os.path.exists(file_name):
            sudoku = file_holder(file_name)
            coordinates = get_coordinates(sudoku)
            # Use Brute Force or Backtracking solver
            back_or_brute = input("Select 1 for the Brute Force solution or 2 for the Backtrack solution: ")
            if back_or_brute == 1:
                solver = BruteForce(sudoku)
            else:
                solver = Backtracking(sudoku)
            if solver.solve(sudoku):
                print(print_grid(solver.grid, coordinates))
            else:
                print("No solution found.")
            choice = input("Do you want to solve another one? (y/n) ")
            if choice.lower() not in ['y', 'yes']:
                print("See ya!")
                break

if __name__ == "__main__":
    execute()


