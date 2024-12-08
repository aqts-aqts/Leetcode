class Solution(object):
    def maxSubArray(self, nums):
        n = len(nums)
        dp = [0] * n
        dp[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            dp[i] = max(nums[i] + dp[i + 1], nums[i])
        return max(dp)