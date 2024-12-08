class Solution:
    def PredictTheWinner(self, nums: list[int]) -> bool:
        # let dp[i][j][k] be the relative score of player 1 between i and j as player k's turn
        n = len(nums)
        dp = [[[0, 0] for i in range(n)] for i in range(n)]
        for i in range(n - 1, -1, -1):
            dp[i][i][0] = nums[i]
            dp[i][i][1] = -nums[i]
            for j in range(i + 1, n):
                dp[i][j][0] = max(dp[i + 1][j][1] + nums[i], dp[i][j - 1][1] + nums[j])
                dp[i][j][1] = min(dp[i + 1][j][0] - nums[i], dp[i][j - 1][0] - nums[j])
        return dp[0][n - 1][0] >= 0