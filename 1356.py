# Sort Integers by The Number of 1 Bits
class Solution:
    def sortByBits(self, arr):
        return sorted(arr, key=lambda x: (str(bin(x))[2:].count('1'), x))