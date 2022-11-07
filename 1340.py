# Jump Game V
dp = []
def solve(i, d, arr):
    if dp[i] >= 0: return dp[i]
    if (i == 0 or arr[i - 1] > arr[i]) and (i == len(arr) - 1 or arr[i + 1] > arr[i]): return 1
    maxJump = 0
    for j in range(i + 1, i + d + 1):
        if j >= len(arr): break
        if arr[j] >= arr[i]: break
        maxJump = max(maxJump, solve(j, d, arr))
    for j in range(i - 1, i - d - 1, -1):
        if j < 0: break
        if arr[j] >= arr[i]: break
        maxJump = max(maxJump, solve(j, d, arr))
    dp[i] = maxJump + 1
    return dp[i]

class Solution(object):
    def maxJumps(self, arr, d):
        global dp
        dp = [-1] * len(arr)
        maxVisits = 1
        for i in range(len(arr)):
            maxVisits = max(maxVisits, solve(i, d, arr))
        return maxVisits