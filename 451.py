# Sort Characters By Frequency
from collections import defaultdict
class Solution:
    def frequencySort(self, s):
        cMap = defaultdict(int)
        for c in s: cMap[c] += 1
        return ''.join(sorted(s, reverse=True, key=lambda x: (cMap[x], x)))