class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        for i in range(len(nums)):
            nums[i] **= 2
        n = sorted(nums)
        return n