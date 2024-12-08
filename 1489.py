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

def findMST(vertices, edges):
    unionFind = UnionFind()
    for v in range(vertices):
        unionFind.add(v)
    i, e = 0, 0
    result = []
    while e < vertices - 1:
        try: u, v = edges[i][0], edges[i][1]
        except IndexError: return None
        x = unionFind.find(u)
        y = unionFind.find(v)
        if x != y:
            result.append(edges[i])
            unionFind.union(u, v)
            e += 1
        i += 1
    return result

def findMSTwithEdge(vertices, edges, edge):
    unionFind = UnionFind()
    for v in range(vertices):
        unionFind.add(v)
    i, e = 0, 1
    result = []
    unionFind.union(edges[edge][0], edges[edge][1])
    result.append(edges[edge])
    while e < vertices - 1:
        u, v = edges[i][0], edges[i][1]
        x = unionFind.find(u)
        y = unionFind.find(v)
        if x != y:
            result.append(edges[i])
            unionFind.union(u, v)
            e += 1
        i += 1
    return result

class Solution(object):
    def findCriticalAndPseudoCriticalEdges(self, n, edges):
        for i in range(len(edges)): edges[i].append(i)
        edges = sorted(edges, key = lambda edge: edge[2])

        mst = findMST(n, edges)
        cost = sum(edge[2] for edge in mst)
        pseudo = set()
        critical = set()

        for i in range(len(edges)):
            crit = findMST(n, edges[:i] + edges[i + 1:])
            if crit is None: 
                critical.add(edges[i][3])
                continue
            critCost = sum(edge[2] for edge in crit)
            if critCost > cost: 
                critical.add(edges[i][3])
                continue

            pseu = findMSTwithEdge(n, edges, i)
            pseuCost = sum(edge[2] for edge in pseu)
            if pseuCost == cost: pseudo.add(edges[i][3])

        return [critical, pseudo]