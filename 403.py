# Frog Jump
dp = dict()
def solve(c, k, end, stones):
    if (c, k) in dp: return dp[(c, k)]
    if c not in stones: dp[(c, k)] = False; return False
    if c == end: dp[(c, k)] = True; return True
    dp[(c, k)] = (solve(c + k, k - 1, end, stones) if k > 1 else False) or solve(c + k, k, end, stones) or solve(c + k, k + 1, end, stones)
    return dp[(c, k)]

class Solution:
    def canCross(self, stones):
        global dp
        dp = dict()
        return solve(stones[0], 1, max(stones), stones)