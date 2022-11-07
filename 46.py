# Permutations
class Solution(object):
    def permute(self, nums):
        return [[num] + perm for i, num in enumerate(nums) for perm in self.permute(nums[:i] + nums[i + 1:])] or [[]]