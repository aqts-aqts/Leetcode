from collections import defaultdict

class Solution:
    def groupThePeople(self, groupSizes):
        groups = defaultdict(set)
        result = []

        n = len(groupSizes)
        for i in range(n):
            cur = groupSizes[i]
            m = len(groups[cur])

            if m + 1 == cur:
                groups[cur].add(i)
                result.append(groups[cur]) 
                groups[cur] = set()
            else:
                groups[cur].add(i)
        return result