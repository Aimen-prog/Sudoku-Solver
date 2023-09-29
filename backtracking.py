class Backtracking:

    def __init__(self, grid):
        self.grid = grid

    @staticmethod
    def isEmpty(grid):
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    return (i, j)

    def isValid(self, grid, nb, pos):
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
