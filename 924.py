from collections import deque, defaultdict
class Solution:
    def solve(self, initial, network, n):
        if not initial:
            return 0

        m = len(initial)
        queue = deque()
        visited = set()

        i = 0
        queue.append(initial[i])
        visited.add(initial[i])
        total = 0
        while queue:
            cur = queue.popleft()
            total += 1
            for c in network[cur] - visited:
                queue.append(c)
                visited.add(c)
            if not queue:  
                while initial[i] in visited:
                    i += 1
                    if i == m:
                        return total
                queue.append(initial[i])
                visited.add(initial[i])
        return total

    def minMalwareSpread(self, graph, initial):
        n = len(graph)
        network = defaultdict(set)
        for i in range(n):
            for j in range(n):
                if graph[i][j] and i != j:
                    network[i].add(j)
                    network[j].add(i)
        print(network)
        
        min_infected = float('inf')
        min_node = float('inf')
        for i, node in enumerate(initial):
            infected = self.solve(initial[:i] + initial[i + 1:], network, n)
            print(infected)
            if infected <= min_infected:
                if infected == min_infected:
                    min_node = min(min_node, node)
                else:
                    min_node = node
                min_infected = infected
        return min_node
    
s = Solution()
print(s.minMalwareSpread([[1,1,0],[1,1,0],[0,0,1]], [0,1,2]))