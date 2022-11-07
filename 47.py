class Solution(object):
    def permuteUnique(self, nums):
        if not nums: return []
        return self.permute(sorted(nums))
        
    def permute(self, nums):
        if len(nums) == 1: return [nums]
        r = []    
        for index, num in enumerate(nums):
            if index > 0 and nums[index - 1] == num: continue
            r += [[num] + p for p in self.permute(nums[:index] + nums[index + 1:])]
        return r