import os
import numpy as np
from backtracking import Backtracking
from bruteForce import BruteForce


def file_holder(file_name):
    with open(file_name, 'r') as f:
        file = f.read()
    file = file.replace(' ', '').replace('\n', '').replace('_', "0")
    return (np.array(list(file)).astype(int)).reshape((9, 9))


def get_coordinates(grid):
    coordinates = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] > 0:
                coordinates.append((i, j))
    return coordinates


def print_grid(grid, coordinates):
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

execute()


