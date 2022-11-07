# Minimum Path Cost in a Grid
class Solution:
    def minPathCost(self, grid, moveCost):
        m = len(grid)
        n = len(grid[0])
        dp = [[None for _ in range(n)] for _ in range(m)]
        def solve(r, c):
            if r == m - 1: return grid[r][c]
            if dp[r][c]: return dp[r][c]
            dp[r][c] = min(solve(r + 1, i) + moveCost[grid[r][c]][i] for i in range(n)) + grid[r][c]
            return dp[r][c]
        return min(solve(0, i) for i in range(n))