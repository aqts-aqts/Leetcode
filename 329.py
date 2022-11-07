# Longest Increasing Path in a Matrix
dp = []
def solve(m, n, r, c, matrix):
    if r < 0 or r >= m or c < 0 or c >= n: return 0
    if dp[r][c] > 0: return dp[r][c]
    up = solve(m, n, r - 1, c, matrix) if r - 1 >= 0 and matrix[r - 1][c] > matrix[r][c] else 0
    down = solve(m, n, r + 1, c, matrix) if r + 1 < m and matrix[r + 1][c] > matrix[r][c] else 0
    right = solve(m, n, r, c + 1, matrix) if c + 1 < n and matrix[r][c + 1] > matrix[r][c] else 0
    left = solve(m, n, r, c - 1, matrix) if c - 1 >= 0 and matrix[r][c - 1] > matrix[r][c] else 0
    dp[r][c] = max(up, down, right, left) + 1
    return dp[r][c]

class Solution:
    def longestIncreasingPath(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        global dp
        dp = [[0 for _ in range(n)] for _ in range(m)]
        maxPath = 0
        for i in range(m):
            for j in range(n):
                path = solve(m, n, i, j, matrix)
                if path > maxPath: maxPath = path
        return maxPath