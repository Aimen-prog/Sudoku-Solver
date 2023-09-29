import os, time
import numpy as np
from backtracking import Backtracking
from bruteForce import BruteForce

def file_holder(file_name):
    with open(file_name, 'r') as f:
        file = f.read()
    file = file.replace(' ', '').replace('\n', '').replace('_', "0")
    return (np.array(list(file)).astype(int)).reshape((9, 9))
def benchmark_all_puzzles():
    puzzle_directory = "./sudoku_puzzles"
    puzzle_files = os.listdir(puzzle_directory)
    brute_force_times = []
    backtracking_times = []

    for puzzle_file in puzzle_files:
        puzzle_path = os.path.join(puzzle_directory, puzzle_file)

        if os.path.isfile(puzzle_path):
            sudoku = file_holder(puzzle_path)
            back_or_brute = input("Select 1 for the Brute Force solution or 2 for the Backtrack solution: ")

            if back_or_brute == '1':
                solver = BruteForce(sudoku)
            else:
                solver = Backtracking(sudoku)

            start_time = time.time()
            if solver.solve(sudoku):
                end_time = time.time()
                execution_time = end_time - start_time

                print(f"Solved {puzzle_file} in {execution_time} seconds")

                if back_or_brute == '1':
                    brute_force_times.append(execution_time)
                else:
                    backtracking_times.append(execution_time)
            else:
                print(f"No solution found for {puzzle_file}")
    #calculate and print average execution times for all puzzles
    if brute_force_times:
        avg_brute_force_time = sum(brute_force_times) / len(brute_force_times)
        print(f"Average Brute Force execution time: {avg_brute_force_time} seconds")

    if backtracking_times:
        avg_backtracking_time = sum(backtracking_times) / len(backtracking_times)
        print(f"Average Backtracking execution time: {avg_backtracking_time} seconds")


benchmark_all_puzzles()