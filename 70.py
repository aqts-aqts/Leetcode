# Climbing Stairs
class Solution:
    def climbStairs(self, n):
        dp = dict()
        def solve(num, n):
            if num == n: return 1
            elif num > n: return 0
            if num in dp: return dp[num]
            dp[num] = solve(num + 1, n) + solve(num + 2, n)
            return dp[num]
        return solve(0, n)