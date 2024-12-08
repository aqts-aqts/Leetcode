class Solution:
    def generate(self, n: int) -> list[list[int]]:
        dp = [[0] * n for i in range(n)]
        dp[0][0] = 1

        for i in range(1, n):
            for j in range(i + 1):
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
        
        result = []
        for row in dp:
            result.append([num for num in row if num])
        return result