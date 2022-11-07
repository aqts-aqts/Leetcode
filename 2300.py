# Successful Pairs of Spells and Potions
from bisect import bisect_left
class Solution:
    def successfulPairs(self, spells, potions, success):
        n = len(potions)
        pairs = []
        potions.sort()
        for spell in spells:
            cap = success / spell
            pairs.append(n - bisect_left(potions, cap))
        return pairs