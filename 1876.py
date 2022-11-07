# Substrings of Size Three with Distinct Characters
class Solution:
    def countGoodSubstrings(self, s):
        ss = 0
        for i in range(2, len(s)):
            if s[i - 2] != s[i - 1] and s[i - 1] != s[i] and s[i] != s[i - 2]: 
                ss += 1
        return ss