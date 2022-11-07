# Largest Rectangle in Histogram
class Rectangle:
    def __init__(self, index, height):
        self.index = index
        self.height = height
    def area(self, end):
        return self.height * (end - self.index)

def solve(heights):
    stack = []
    area = 0
    for i in range(len(heights)):
        start = i
        while stack and stack[-1].height > heights[i]:
            cur = stack.pop()
            area = max(area, cur.area(i))
            start = cur.index
        stack.append(Rectangle(start, heights[i]))
    for cur in stack:
        area = max(area, cur.area(len(heights)))
    return area

class Solution(object):
    def largestRectangleArea(self, heights):
        return solve(heights)