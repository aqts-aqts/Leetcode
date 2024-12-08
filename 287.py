class Solution:
    def findDuplicate(self, nums):
        found = {}
        n = len(nums)
        for i in range(n):
            num = nums[i]
            if nums[i] in found:
                return nums[i]
            found[nums[i]] = 1
        