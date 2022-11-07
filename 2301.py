# Match Substring After Replacement
from collections import defaultdict
class Solution:
    def matchReplacement(self, s, sub, mappings):
        maps = defaultdict(set)
        for m in mappings:
            maps[m[0]].add(m[1])

        n = len(sub)
        for i in range(len(s) - n + 1):
            string = s[i:i + n]
            valid = True
            for j in range(n):
                if string[j] == sub[j]: continue
                if not string[j] in maps[sub[j]]:
                    valid = False 
                    break
            if valid: return True
        return False