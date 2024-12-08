from typing import List

class UnionFind:
    def __init__(self):
        self.parent = dict()
        self.rank = dict()
        self.leftmost = dict()
        self.rightmost = dict()
    def add(self, val, left, right):
        self.parent[val] = val
        self.rank[val] = 0
        self.leftmost[val] = left
        self.rightmost[val] = right
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
                self.leftmost[x] = min(self.leftmost[y], self.leftmost[x])
                self.rightmost[x] = max(self.rightmost[y], self.rightmost[x])
            elif self.rank[x] < self.rank[y]:
                self.parent[x] = y
                self.leftmost[y] = min(self.leftmost[y], self.leftmost[x])
                self.rightmost[y] = max(self.rightmost[y], self.rightmost[x])
            else:
                self.parent[x] = y
                self.leftmost[y] = min(self.leftmost[y], self.leftmost[x])
                self.rightmost[y] = max(self.rightmost[y], self.rightmost[x])
                self.rank[y] += 1

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        letter_pairs = {}
        for i,c in enumerate(s):
            if c in letter_pairs:
                letter_pairs[c][1] = i
            else:
                letter_pairs[c] = [i, i]
            
        uf = UnionFind()
        for c in letter_pairs:
            uf.add(c, letter_pairs[c][0], letter_pairs[c][1])
        
        for c in letter_pairs:
            for k in letter_pairs:
                a = uf.find(c)
                b = uf.find(k)
                if a == b:
                    continue
                
                if uf.leftmost[a] < uf.leftmost[b] < uf.rightmost[a] or uf.leftmost[b] < uf.leftmost[a] < uf.rightmost[b]:
                    uf.union(c, k)
        
        l = []
        for c in uf.parent:
            if uf.parent[c] == c:
                l.append((uf.leftmost[c], uf.rightmost[c]))
        
        ans = []
        l.sort()
        for x in l:
            ans.append(x[1] - x[0] + 1)
        return ans
