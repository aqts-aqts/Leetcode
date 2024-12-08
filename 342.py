class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        for i in range(16):
            if 4 ** i == n: return 1
        return 0