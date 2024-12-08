from collections import defaultdict

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        ransomMap = defaultdict(int)
        magaMap = defaultdict(int)
        for c in ransomNote:
            if c in ransomMap:
                ransomMap[c] += 1
            else:
                ransomMap[c] = 1
        for c in magazine:
            if c in magaMap:
                magaMap[c] += 1
            else:
                magaMap[c] = 1
        for key in ransomMap:
            if magaMap[key] < ransomMap[key]:
                return False
        return True