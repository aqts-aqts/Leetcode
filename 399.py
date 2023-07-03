from collections import deque, defaultdict

class Solution(object):
    def bfs(self, graph, query):
        n1, n2 = query
        if n1 not in graph or n2 not in graph:
            return -1

        queue = deque()
        product = deque()
        queue.append(n1)
        product.append(1)

        visited = set()
        visited.add(n1)

        while queue:
            cur = queue.popleft()
            res = product.popleft()

            if cur == n2:
                return res

            for n in graph[cur]:
                num, val = n
                if num not in visited:
                    visited.add(num)
                    queue.append(num)
                    product.append(res * val)
        return -1

    def calcEquation(self, equations, values, queries):
        graph = defaultdict(set)

        for i, e in enumerate(equations):
            n1, n2 = e
            graph[n1].add((n2, values[i]))
            graph[n2].add((n1, 1 / values[i]))
        
        result = []
        for query in queries:
            result.append(self.bfs(graph, query))
        return result