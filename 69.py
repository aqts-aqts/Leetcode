# Sqrt(x)
class Solution:
    def mySqrt(self, x):
        def binarySearch(low, high):
            if low <= high:
                mid = (low + high) // 2
                if mid * mid > x: return binarySearch(low, mid - 1)
                elif mid * mid < x: return binarySearch(mid + 1, high)
                else: return mid
            return high
        return binarySearch(1, x)