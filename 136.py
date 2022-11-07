# Single Number
class Solution:
    def singleNumber(self, nums):
        n = 0
        for num in nums: n ^= num
        return n