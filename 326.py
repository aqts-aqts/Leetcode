# Power of Three
class Solution(object):
    def isPowerOfThree(self, n):
        for i in range(20):
            if 3 ** i == n: return True
        return False