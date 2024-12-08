class Solution(object):
    def firstMissingPositive(self, nums):
        n = len(nums) # O(n)
        i = 0
        while i < n:
            x = nums[i]
            if x > 0 and x <= n and nums[x - 1] != x:
                nums[i], nums[x - 1] = nums[x - 1], nums[i]
            else:
                i += 1
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1