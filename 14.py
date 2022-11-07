# Longest Common Prefix
class Solution:
    def longestCommonPrefix(self, strs):
        prefix = ''
        for i in range(len(min(strs, key=lambda x: len(x)))):
            cur = strs[0][i]
            for j in range(1, len(strs)):
                if strs[j][i] != cur: return prefix
            prefix += cur
        return prefix