from collections import defaultdict
class Solution(object):
    def maxPoints(self, points):
        n = len(points)
        if n == 1: return 1

        def getSlopeIntercept(point1, point2):
            try: slope = float(point1[1] - point2[1]) / float(point1[0] - point2[0])
            except ZeroDivisionError: slope = None

            try: intercept = point1[1] - slope * point1[0]
            except TypeError: intercept = point1[0]
            return (slope, intercept)

        lines = defaultdict(set)
        for i in range(n - 1):
            for j in range(i + 1, n):
                slopeIntercept = getSlopeIntercept(points[i], points[j])
                lines[slopeIntercept].add(i)
                lines[slopeIntercept].add(j)

        line = 0
        for l in lines.values(): line = max(len(l), line)
        return line