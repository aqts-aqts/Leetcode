from sys import maxsize as inf
class Solution(object):
    def minPathSum(self, grid):
        m = len(grid[0])
        n = len(grid)
        dp = [[None] * m for i in range(n)]
        def solve(i, j):
            if i == n - 1 and j == m - 1: return grid[i][j]
            elif i == n or j == m: return inf
            elif dp[i][j] is not None: return dp[i][j]
            dp[i][j] = min(solve(i + 1, j) + grid[i][j], solve(i, j + 1) + grid[i][j])
            return dp[i][j]
        return solve(0, 0)