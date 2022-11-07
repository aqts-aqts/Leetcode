# Regular Expression Matching
def solve(s, p, P=0, begin=0, end=0):
    print(P, begin, end)
    if P >= len(p) and end >= len(s): return True
    elif P >= len(p): return False
    match = p[P] if p[P] != '.' else 'abcdefghijklmnopqrstuvwxyz'
    if len(p) > 1 and P < len(p) - 1 and p[P + 1] == '*':
        if end < len(s):
            while s[end] in match:
                if end < len(s): end += 1
                if end >= len(s): break
        return solve(s, p, P + 2, begin, end)
    else:
        if begin >= len(s): return False
        for i in range(begin, end + 1):
            if i > len(s) - 1: break
            if s[i] in match:
                if solve(s, p, P + 1, i + 1, i + 1): return True
    return False

class Solution(object):
    def isMatch(self, s, p):
        return solve(s, p)