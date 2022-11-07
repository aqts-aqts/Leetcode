# Jump Game II
INF = int(1e9)
dp = []
def solve(index, nums):
    if dp[index] < INF: return dp[index]
    jump = nums[index]
    if not jump: return INF
    if index + jump >= len(nums) - 1: return 1
    steps = INF
    for i in range(1, jump + 1):
        steps = solve(index + i, nums) + 1
        if dp[index] > steps: dp[index] = steps
    return dp[index]

class Solution(object):
    def jump(self, nums):
        if len(nums) == 1: return 0
        global dp
        dp = [INF] * len(nums)
        return solve(0, nums)