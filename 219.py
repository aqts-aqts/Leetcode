# Contains Duplicate II
class Solution:
    def containsNearbyDuplicate(self, nums, k):
        index = dict()
        for i, n in enumerate(nums):
            if n in index and i - index[n] <= k: return True
            index[n] = i
        return False