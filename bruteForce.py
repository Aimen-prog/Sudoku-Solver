
class BruteForce:
    def __init__(self, grid):
        self.grid = grid
        self.counter = 0

    def solve(self, grid):
        """
        Attempt to solve the Sudoku puzzle using a brute force approach.

        Parameters:
        - grid (list of lists): The 9x9 Sudoku grid to be solved.

        Returns:
        - bool: True if a valid solution is found and the grid is solved; False otherwise.
        """
        for i in range(9):
            for j in range(9):
                if grid[i][j] == 0:
                    for k in range(1, 10):
                        if self.check(grid, i, j, k):
                            grid[i][j] = k
                            self.counter += 1
                            if self.solve(grid):
                                return True
                            else:
                                grid[i][j] = 0
                                self.counter -= 1
                    return False
        return True

    def check(self, grid, row, column, num):
        """
        Check if it's valid to place a number at a specific position in the Sudoku grid.

        Parameters:
        - grid (list of lists): The 9x9 Sudoku grid to be checked.
        - row (int): The row index of the cell being checked.
        - column (int): The column index of the cell being checked.
        - num (int): The number to be checked for validity.

        Returns:
        - bool: True if placing the number at the specified position is valid;
          False otherwise.

        """
        if num in grid[row]:
            return False
        for i in range(9):
            if grid[i][column] == num:
                return False

        x = (row - (row % 3))
        y = (column - (column % 3))

        for i in range(3):
            for j in range(3):
                if (i, j) == (row, column):
                    continue
                if grid[x + j][y + i] == num:
                    return False
        return True