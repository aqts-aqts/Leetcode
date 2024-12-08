class Solution(object):
    def isIsomorphic(self, s, t):
        bijects = {}
        chars = set()
        n = len(s)
        for i in range(n):
            if s[i] not in bijects:
                if t[i] in chars: return False
                chars.add(t[i])
                bijects[s[i]] = t[i]
            elif bijects[s[i]] != t[i]: return False
        return True