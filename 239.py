import heapq

class Solution:
    def maxSlidingWindow(self, nums, k):
        n = len(nums)
        queue = [(-num, i) for i, num in enumerate(nums[:k])]
        heapq.heapify(queue)
        windows = []
        windows.append(-queue[0][0])

        for i in range(k, n):
            heapq.heappush(queue, (-nums[i], i))
            while queue[0][1] <= i - k:
                heapq.heappop(queue)
            windows.append(-queue[0][0])
        return windows