class Solution(object):
    def minCut(self, s):
        def isPalindrome(string): return string == string[::-1]
        n = len(s)
        dp = [0] * n

        for i in range(n):
            minCut = i
            for j in range(i + 1):
                if isPalindrome(s[j:i + 1]):
                    minCut = 0 if j == 0 else min(minCut, dp[j - 1] + 1)
            dp[i] = minCut
        return dp[n - 1]