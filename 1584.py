class Solution(object):
    def uniquePathsWithObstacles(self, grid):
        n = len(grid)
        m = len(grid[0])
        dp = dict()
        if grid[n - 1][m - 1]: return 0
        def solve(row, col):
            if (row, col) == (n - 1, m - 1): return 1
            elif row == n or col == m or grid[row][col]: return 0
            elif (row, col) in dp: return dp[(row, col)]
            dp[(row, col)] = solve(row + 1, col) + solve(row, col + 1)
            return dp[(row, col)]
        return solve(0, 0)