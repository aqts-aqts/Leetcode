from collections import defaultdict

class Solution:
    def BFS(self, start: int, graph: dict[int, set[int]], targets: set[int]):
        queue = [start]
        dists = [1]
        visited = set()
        while queue:
            cur = queue.pop()
            dist = dists.pop()
            if cur in targets:
                return dist
            for stop in graph[cur] - visited:
                queue.append(stop)
                dists.append(dist + 1)
                visited.add(stop)
        return 1e10

    def numBusesToDestination(self, routes: list[list[int]], source: int, target: int) -> int:
        if source == target:
            return 0

        # just bfs lmao
        # okay maybe making the bfs graph would take too long

        graph = defaultdict(set)
        targets = set()
        sources = set()

        for i, route in enumerate(routes):
            if target in route:
                targets.add(i)
            if source in route:
                sources.add(i)
        
        if not sources or not targets:
            return -1
        print(targets, sources)
        n = len(routes)

        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                bus_stops = set()
                for k in range(len(routes[i])):
                    bus_stops.add(routes[i][k])
                for k in range(len(routes[j])):
                    if routes[j][k] in bus_stops:
                        graph[i].add(j)
                        graph[j].add(i)
                        break
        
        print(graph)
        ans = min(self.BFS(s, graph, targets) for s in sources)
        return ans if ans < 1e9 else -1