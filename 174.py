# Dungeon Game
INF = 1e9
dp = []
def solve(r, c, rows, cols, dungeon):
    global dp
    if r >= rows or c >= cols: return INF
    if r == rows - 1 and c == cols - 1: return 1 if dungeon[r][c] > 0 else abs(dungeon[r][c]) + 1
    if dp[r][c] != -1: return dp[r][c]
    right = solve(r, c + 1, rows, cols, dungeon) - dungeon[r][c]
    down = solve(r + 1, c, rows, cols, dungeon) - dungeon[r][c]
    dp[r][c] = min(1 if right <= 0 else right, 1 if down <= 0 else down)
    return dp[r][c]
class Solution:
    def calculateMinimumHP(self, dungeon):
        global dp
        rows = len(dungeon)
        cols = len(dungeon[0])
        dp = [[-1 for _ in range(cols)] for _ in range(rows)]
        return solve(0, 0, rows, cols, dungeon)