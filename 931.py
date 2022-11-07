# Minimum Falling Path Sum
from sys import maxsize as MAX
class Solution:
    def minFallingPathSum(self, grid):
        for i in range(1, len(grid)):
            for j in range(len(grid)): grid[i][j] = min(grid[i - 1][j - 1] if j > 0 else MAX, grid[i - 1][j], grid[i - 1][j + 1] if j < len(grid) - 1 else MAX) + grid[i][j]
        return min(grid[len(grid) - 1])