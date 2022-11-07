# Jump Game VI
from heapq import heappop as pop
from heapq import heappush as push
MIN = -1e9
class Solution(object):
    def maxResult(self, nums, k):
        dp = [MIN] * len(nums)
        heap = [(-nums[-1], len(nums) - 1)]
        dp[-1] = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            score, index = heap[0]
            while index > i + k:
                pop(heap)
                score, index = heap[0]
            dp[i] = -score + nums[i]
            push(heap, (-dp[i], i))
        return dp[0]