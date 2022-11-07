# Minimum Index Sum of Two Lists
class Solution:
    def findRestaurant(self, list1, list2):
        isum = {}
        minval = 1e9
        for i, s in enumerate(list1):
            isum[s] = i
        for i, s in enumerate(list2):
            if s not in isum: continue
            minval = min(minval, isum[s] + i)
            isum[s] += i
        mins = []
        for key in isum:
            if isum[key] == minval and key in list2: mins.append(key)
        return mins