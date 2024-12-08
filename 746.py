class Solution(object):
    def minCostClimbingStairs(self, cost):
        n = len(cost)
        dp = [0] * (n + 2)
        for i in range(n - 1, -1, -1):
            dp[i] = min(dp[i + 2], dp[i + 1]) + cost[i]
        return min(dp[0], dp[1])