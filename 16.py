# 3Sum Closest
from sys import maxsize as MAX
class Solution:
    def threeSumClosest(self, nums, target):
        distance = MAX
        num = 0
        nums.sort()
        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                if abs(target - (nums[i] + nums[left] + nums[right])) < distance:
                    distance = abs(target - (nums[i] + nums[left] + nums[right]))
                    num = nums[i] + nums[left] + nums[right]
                if nums[i] + nums[left] + nums[right] < target: left += 1
                elif nums[i] + nums[left] + nums[right] > target: right -= 1
                else: return target
        return num