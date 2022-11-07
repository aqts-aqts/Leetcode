# Search Insert Position
class Solution:
    def searchInsert(self, nums, target):
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] < target: 
                if low == high: return mid + 1
                low = mid + 1
            elif nums[mid] > target:
                if low == high: return mid
                high = mid
            else: return mid