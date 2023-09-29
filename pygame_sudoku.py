import pygame
import os
import numpy as np
from backtracking import Backtracking
from bruteForce import BruteForce
import tkinter as tk
from tkinter import filedialog, simpledialog

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

## initialize Pygame
pygame.init()
WIDTH, HEIGHT = 600, 600
GRID_SIZE = 9
CELL_SIZE = WIDTH // GRID_SIZE
FPS = 60
WHITE = (255, 255, 255)
FONT_SIZE = 36

#create a Pygame window
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku Solver")
font = pygame.font.Font(None, FONT_SIZE)

def draw_grid(grid, coordinates):
    window.fill(WHITE)
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            x = j * CELL_SIZE
            y = i * CELL_SIZE
            pygame.draw.rect(window, (0, 0, 0), (x, y, CELL_SIZE, CELL_SIZE), 1)

            if grid[i][j] != 0:
                text = font.render(str(grid[i][j]), True, (0, 0, 0))
                text_rect = text.get_rect(center=(x + CELL_SIZE // 2, y + CELL_SIZE // 2))
                window.blit(text, text_rect)

    # Highlight the given coordinates
    for coord in coordinates:
        i, j = coord
        pygame.draw.rect(window, (0, 255, 0), (j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE), 2)

    pygame.display.flip()

def brute_or_backtrack():
    root = tk.Tk()
    root.withdraw()
    choice = simpledialog.askstring("Solving Method", "Enter 1 for the Brute Force solution or 2 for the Backtrack solution:")
    try:
        choice = int(choice)
        if choice == 1 or choice == 2:
            return choice
        else:
            raise ValueError("Invalid choice")
    except (ValueError, TypeError):
        return None

def execute():
    # Create a Tkinter root window (it will be hidden)
    root = tk.Tk()
    root.withdraw()  # Hide the main root window

    # Use a file dialog to select a file
    file_name = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])

    if file_name:
        if os.path.exists(file_name):
            sudoku = file_holder(file_name)
            coordinates = get_coordinates(sudoku)

            solver_choice = brute_or_backtrack()

            if solver_choice == 1:
                solver = BruteForce(sudoku)
            else:
                solver = Backtracking(sudoku)

            running = True
            while running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                if solver.solve(sudoku):
                    draw_grid(solver.grid, coordinates)

if __name__ == "__main__":
    pygame.init()
    execute()
    pygame.quit()