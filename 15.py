# 3Sum
class Solution:
    def threeSum(self, nums):
        triplets = set()
        def twoSum(cur, target):
            Map = dict()
            for i in range(cur + 1, len(nums)):
                if target - nums[i] not in Map: Map[nums[i]] = i
                else: triplets.add(tuple(sorted([nums[cur], nums[i], nums[Map[target - nums[i]]]])))
        
        for i in range(len(nums)): twoSum(i, -nums[i])
        return triplets