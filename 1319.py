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
    def makeConnected(self, n, connections):
        cycles = 0
        uf = UnionFind()
        for i in range(n):
            uf.add(i)

        for connection in connections:
            a, b = connection
            if uf.find(a) != uf.find(b):
                uf.union(a, b)
            else:
                cycles += 1

        components = len(set(uf.find(i) for i in range(n)))
        if cycles >= components - 1:
            return components - 1
        else:
            return -1