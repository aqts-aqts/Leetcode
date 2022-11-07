# Two Sum
class Solution:
    def twoSum(self, nums, target):
        dp = dict()
        for i in range(len(nums)):
            if nums[i] in dp: return [dp[nums[i]], i]
            else: dp[target - nums[i]] = i