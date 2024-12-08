class Solution(object):
    def wordPattern(self, pattern, s):
        patterns = {}
        n = len(pattern)
        words = s.split()
        if len(words) != n: return False
        for i in range(n):
            if pattern[i] in patterns:
                if words[i] != patterns[pattern[i]]:
                    return False
            else:
                if words[i] in patterns.values(): return False
                patterns[pattern[i]] = words[i]
        return True