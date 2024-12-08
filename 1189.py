from collections import defaultdict

class Solution(object):
    def maxNumberOfBalloons(self, text):
        charMap = defaultdict(int)
        for c in text:
            charMap[c] += 1

        b = charMap['b']
        a = charMap['a']
        l = charMap['l'] // 2
        o = charMap['o'] // 2
        n = charMap['n']
        return min(b, a, l, o, n)