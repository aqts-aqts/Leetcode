# Jump Game
dp = []
def solve(index, nums):
    if dp[index] >= 0: return dp[index]
    jump = nums[index]
    if index + jump >= len(nums) - 1:
        dp[index] = True
        return True
    for i in range(jump, 0, -1):
        if solve(index + i, nums): 
            dp[index] = True
            return True
    dp[index] = False
    return False

class Solution(object):
    def canJump(self, nums):
        if len(nums) == 1: return True
        global dp
        dp = [-1] * len(nums)
        return solve(0, nums)