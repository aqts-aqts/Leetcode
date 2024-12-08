from bisect import bisect_left
class Solution:
    def mincostTickets(self, days, costs):
        n = len(days)
        dp = [None] * n
        def solve(i):
            if i == n:
                return 0
            elif dp[i] is not None:
                return dp[i]
            
            dp[i] = min(solve(i + 1) + costs[0], solve(bisect_left(days, days[i] + 7)) + costs[1], solve(bisect_left(days, days[i] + 30)) + costs[2])
            return dp[i]
        return solve(0)