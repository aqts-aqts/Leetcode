class Solution(object):
    dp = [0] * 50

    def tribonacci(self, n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 1
        elif self.dp[n]:
            return self.dp[n]
        
        self.dp[n] = self.tribonacci(n - 3) + self.tribonacci(n - 2) + self.tribonacci(n - 1)
        return self.dp[n]