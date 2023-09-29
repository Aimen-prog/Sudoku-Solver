
class BruteForce:
    def __init__(self, grid):
        self.grid = grid
        self.counter = 0

    def solve(self, grid):
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