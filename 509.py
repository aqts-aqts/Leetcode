class Solution:
    dp = [0] * 31
    def fib(self, n):
        if n < 2:
            return n
        elif self.dp[n]:
            return self.dp[n]
        else:
            self.dp[n] = self.fib(n - 2) + self.fib(n - 1)
            return self.dp[n]