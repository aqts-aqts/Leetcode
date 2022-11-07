# Longest Substring Without Repeating Characters
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if not len(s): return 0
        state = dict()
        max = 0
        dist = 0
        for i in range(len(s)):
            if s[i] in state and state[s[i]] > dist: dist += state[s[i]] - dist
            if i - dist + 1 > max: max = i - dist + 1
            state[s[i]] = i + 1
        if i - dist + 1 > max: max = i - dist + 1
        return max