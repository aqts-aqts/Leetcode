# Minimum Falling Path Sum II
class Solution:
    def minFallingPathSum(self, grid):
        for i in range(1, len(grid)):
            for j in range(len(grid)): grid[i][j] = min(grid[i - 1][k] for k in range(len(grid)) if k != j) + grid[i][j]
        return min(grid[len(grid) - 1])