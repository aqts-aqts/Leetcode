# Remove Duplicates from Sorted Array
class Solution:
    def removeDuplicates(self, nums):
        visited = dict()
        i = 0
        while i < len(nums):
            n = nums[i]
            if n in visited: nums.pop(i)
            else: 
                visited[n] = 1
                i += 1