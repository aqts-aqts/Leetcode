# Wildcard Matching
class Solution(object):
    def isMatch(self, s, p):
        # case 1: first character is not a star
        # case 2: last character is not a star
        # case 3: both first and last characters are stars

        if not s and not p: return True
        elif not p: return False
        n = len(s)
        m = len(p)

        temp = p[0] # remove duplicate stars
        for i in range(1, m):
            if p[i] == '*' and temp[-1] != '*': temp += p[i]
            elif p[i] != '*': temp += p[i]
        p = temp

        if p == '*': return True

        if p[0] != '*': # case 1
            i = 0
            while i < n and i < m and p[i] != '*':
                if s[i] != p[i] and p[i] != '?': return False
                i += 1
            s = s[i:]
            p = p[i:]

        if p == '*': return True
        if not s and not p: return True
        elif not s or not p: return False
        n = len(s)
        m = len(p)

        if p[-1] != '*': # case 2
            i = 1
            while n - i >= 0 and m - i >= 0 and p[m - i] != '*':
                if s[n - i] != p[m - i] and p[m - i] != '?': return False
                i += 1
            s = s[:n - i + 1]
            p = p[:m - i + 1]

        if p == '*': return True
        if not s: return False
        n = len(s)
        m = len(p)
        
        # case 3
        sequences = p.split('*')[1:] # find all subsequences
        sequences.pop()
        matches = 0
        prevMatch = -1
        for sequence in sequences:
            for i in range(n - len(sequence) + 1):
                match = 0
                for j in range(i, i + len(sequence)):
                    if s[j] == sequence[j - i] or sequence[j - i] == '?': match += 1
                    else: break
                if match == len(sequence) and i > prevMatch:
                    prevMatch = j # set position of previous match
                    matches += 1
                    break
        if matches == len(sequences): return True
        else: return False