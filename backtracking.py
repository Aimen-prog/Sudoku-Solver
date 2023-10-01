class Backtracking:

    def __init__(self, grid):
        self.grid = grid

    @staticmethod
    def isEmpty(grid):
        """
        Check if a Sudoku grid has an empty cell (cell with value 0).

        Parameters:
        - grid (list of lists): the 9x9 Sudoku grid to check.

        Returns:
        - tuple or None: If an empty cell is found, returns a tuple (row, column)
          containing the coordinates of the first empty cell encountered. If the
          grid has no empty cells, returns None.
        """
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    return (i, j)

    def isValid(self, grid, nb, pos):
        """
        Check if a number can be placed in a Sudoku grid at a specific position.

        Parameters:
        - grid (list of lists): The 9x9 Sudoku grid to check.
        - nb (int): The number to be placed in the grid.
        - pos (tuple): The (row, column) coordinates where the number is to be placed.

        Returns:
        - bool: True if the number can be placed at the given position without violating
          Sudoku rules (no duplicates in the same row, column, or 3x3 subgrid); False otherwise.
        """
        for i in range(len(grid)):
            if grid[i][pos[1]] == nb and pos[0] != i:
                return False
        for i in range(len(grid[0])):
            if grid[pos[0]][i] == nb and pos[1] != i:
                return False
        subgrid_col_index = pos[1] // 3
        subgrid_row_index = pos[0] // 3
        for i in range(subgrid_row_index * 3, subgrid_row_index * 3 + 3):
            for j in range(subgrid_col_index * 3, subgrid_col_index * 3 + 3):
                if grid[i][j] == nb and (i, j) != pos:
                    return False
        return True

    def solve(self, grid):
        """
        Solve a Sudoku puzzle using a backtracking algorithm.

        Parameters:
        - grid (list of lists): The 9x9 Sudoku grid to be solved.

        Returns:
        - bool: True if a valid solution is found and the grid is solved; False otherwise.
        """
        empty = self.isEmpty(grid)
        if not empty:
            return True
        else:
            row, col = empty
        for i in range(1, 10):
            if self.isValid(grid, i, (row, col)):
                grid[row][col] = i
                if self.solve(grid):
                    return True
                grid[row][col] = 0
        return False
