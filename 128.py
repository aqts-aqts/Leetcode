class UnionFind:
    def __init__(self):
        self.parent = dict()
        self.rank = dict()
    def add(self, val):
        self.parent[val] = val
        self.rank[val] = 0
    def find(self, val): 
        if self.parent[val] != val:
            self.parent[val] = self.find(self.parent[val])
        return self.parent[val]
    def union(self, a, b):
        x = self.find(a)
        y = self.find(b)
        if x != y:
            if self.rank[x] > self.rank[y]:
                self.parent[y] = x
            elif self.rank[x] < self.rank[y]:
                self.parent[x] = y
            else:
                self.parent[x] = y
                self.rank[y] += 1

class Solution(object):
    def longestConsecutive(self, nums):
        if not nums: return 0
        nums = set(nums)
        sequences = UnionFind()
        for num in nums:
            if (num - 1) not in sequences.parent and (num + 1) not in sequences.parent:
                sequences.add(num)
            elif (num - 1) in sequences.parent and (num + 1) not in sequences.parent:
                sequences.add(num)
                sequences.union(num - 1, num)
            elif (num - 1) not in sequences.parent and (num + 1) in sequences.parent:
                sequences.add(num)
                sequences.union(num, num + 1)
            else:
                sequences.add(num)
                sequences.union(num - 1, num)
                sequences.union(num, num + 1)
        
        unions = dict()
        for num in nums:
            n = sequences.find(num)
            if n in unions: unions[n] += 1
            else: unions[n] = 1
        return max(unions.values())