# Move Zeroes
class Solution:
    def moveZeroes(self, nums):
        z = 0
        for i in range(len(nums)):
            if not nums[i]: z += 1
        i = 0
        while i < len(nums) and z > 0:
            if not nums[i]:
                nums.append(nums.pop(i))
                i -= 1
                z -= 1
            i += 1
        return nums