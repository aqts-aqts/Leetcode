# 4Sum
class Solution:
    def fourSum(self, nums, target):
        n = len(nums)
        if n < 4: return []

        nums.sort()
        quads = []
        for i in range(n):
            for j in range(n - 1, i, -1):
                left = i + 1
                right = j - 1
                if left == j or right == i: continue
                while left < right:
                    cur = nums[i] + nums[j] + nums[left] + nums[right]
                    if cur == target: quads.append((nums[i], nums[j], nums[left], nums[right]))
                    if cur < target: left += 1
                    else: right -= 1
        return set(quads)