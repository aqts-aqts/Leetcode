class Solution(object):
    def splitArray(self, nums, k):
        n = len(nums)
        dp = [[float('inf')] * (k + 1) for i in range(n + 1)]

        sums = [[0] * n for i in range(n)]
        for i in range(n):
            sums[i][i] = nums[i]
            for j in range(i + 1, n):
                sums[i][j] = sums[i][j - 1] + nums[j]

        for i in range(1, n + 1):
            dp[i][1] = sums[0][i - 1]
            for j in range(2, k + 1):
                for x in range(i):
                    dp[i][j] = min(dp[i][j], max(dp[x][j - 1], sums[x][i - 1]))
        return dp[n][k]