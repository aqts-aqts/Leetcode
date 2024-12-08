class Solution:
  def findMaxK(self, nums: list[int]) -> int:
    s = set(nums)
    return max((x for x in nums if -x in s), default=-1)