# Next Permutation
class Solution:
    def nextPermutation(self, nums):
        if nums == sorted(nums, reverse=True): nums[:] = sorted(nums)
        else:
            i = len(nums) - 1
            while i > 0 and nums[i - 1] >= nums[i]: i -= 1
            if i:
                for j in range(len(nums) - 1, -1, -1):
                    if j >= i and nums[j] > nums[i - 1]:
                        nums[i - 1] = nums[i - 1] + nums[j]
                        nums[j] = nums[i - 1] - nums[j]
                        nums[i - 1] = nums[i - 1] - nums[j]
                        nums[i:] = nums[i:][::-1]
                        return