class Solution(object):
    def rob(self, nums):
        n = len(nums)
        dp = [None] * n
        def solve(i):
            if i >= n: return 0
            elif dp[i] is not None: return dp[i]
            dp[i] = max(solve(i + 2) + nums[i], solve(i + 1))
            return dp[i]
        return solve(0)