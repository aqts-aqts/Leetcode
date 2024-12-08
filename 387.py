from collections import defaultdict

class Solution(object):
    def firstUniqChar(self, s):
        characters = defaultdict(int)
        for c in s:
            characters[c] += 1
        for i, c in enumerate(s):
            if characters[c] < 2:
                return i
        return -1