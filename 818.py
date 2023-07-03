import sys
sys.setrecursionlimit(int(1e9))

class Solution(object):
    def racecar(self, target):
        dp = {}
        def solve(i, speed):
            if i == target:
                return 0
            elif i > target * 2 or i < -target * 2:
                return 1e9
            elif i in dp:
                return dp[i]
            
            dp[i] = min(solve(i + speed, speed * 2), solve(i, -1 if speed > 0 else 1)) + 1
            return dp[i]
        return solve(0, 1)

s = Solution()
print(s.racecar(3))