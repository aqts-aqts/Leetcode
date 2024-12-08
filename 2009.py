import sys
from bisect import bisect_right

class Solution(object):
    def minOperations(self, nums):
        n = len(nums)
        nums = sorted(set(nums))
        m = len(nums)

        min_operations = sys.maxsize
        for i in range(m):
            end = bisect_right(nums, nums[i] + n - 1)
            elements = end - i
            print(end, elements)
            min_operations = min(min_operations, n - elements)
        
        return min_operations