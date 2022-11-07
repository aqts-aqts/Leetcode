# Container With Most Water
class Solution:
    def maxArea(self, height):
        start = 0
        end = len(height) - 1
        water = 0
        while start != end:
            water = max(water, (end - start) * min(height[start], height[end]))
            if height[start] < height[end]: start += 1
            else: end -= 1
        return water