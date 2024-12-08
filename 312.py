class Solution:
    def maxCoins(self, nums):
        n = len(nums)
        nums = [1] + nums + [1]
        # let dp[i][j] be the maximum number of coins you can get from bursting all the balloons between i and j (inclusive)
        dp = [[0] * (n + 2) for i in range(n + 2)]
        for i in range(n, 0, -1):
            for j in range(i, n + 1):
                for k in range(i, j + 1):
                    dp[i][j] = max(dp[i][j], dp[i][k - 1] + nums[i - 1] * nums[k] * nums[j + 1] + dp[k + 1][j])
        return dp[1][n]