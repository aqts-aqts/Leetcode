from sys import maxsize

class Solution:
    def TSP(self, n: int, graph: list[list[int]], prev: int, visited: set[int], dp: dict[tuple[int, frozenset[int]], (int, list[int])]):
        visited_set = frozenset(visited)

        if len(visited) == len(graph):
            return 0, []
        if (prev, visited_set) in dp:
            return dp[(prev, visited_set)]
                    
        min_cost = maxsize
        min_path = []

        for city in range(n):
            if city not in visited:
                new_visited = visited | {city}
                cost, path = self.TSP(n, graph, city, new_visited, dp)
                cost_with_current = graph[prev][city] + cost

                if cost_with_current < min_cost:
                    min_cost = cost_with_current
                    min_path = [city] + path
            
        dp[(prev, visited_set)] = (min_cost, min_path)
        return min_cost, min_path
    
    def shortestSuperstring(self, words: list[str]) -> str:
        # Observation 1: We can reduce the problem to a graph, the distance from word i to word j is the difference in length when word j is appended to word i. If graph[i] = "1234" and graph[j] = "2345", graph[i][j] = 1.
        # Observation 2: We need to find the shortest Hamiltonian Cycle in the graph. That is, the shortest path that we can take to visit every node in the graph. We can use the Held-Karp algorithm for the Travelling Salesman Problem for this.

        n = len(words)
        graph = [[0 for _ in range(n)] for _ in range(n)]

        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                overlap = 0
                
                for k in range(1, min(len(words[i]), len(words[j])) + 1):
                    if words[i][-k:] == words[j][:k]:
                        overlap = k
                graph[i][j] = len(words[j]) - overlap
        
        dp = {}
        min_cost = maxsize
        min_path = None

        for i in range(n):
            _, path = self.TSP(n, graph, i, {i}, dp)
            path = [i] + path
            ans = words[path[0]]
            
            for i in range(1, n):
                prev_word = words[path[i - 1]]
                current_word = words[path[i]]

                overlap = 0
                min_length = min(len(prev_word), len(current_word))
                for j in range(1, min_length + 1):
                    if prev_word[-j:] == current_word[:j]:
                        overlap = j

                ans += current_word[overlap:]
            
            cost = len(ans)
            if cost < min_cost:
                min_cost = cost
                min_path = ans

        return min_path
    
s = Solution()
print(s.shortestSuperstring(["txvteggrtmylrxxknwub","lipgamrjnsfcqizch","teggrtmylrxxknwubv","uogduurswxthftx","akwnbruogduursw","uurswxthftxvteg","mylrxxknwubvlipga","ggrtmylrxxknwubvl","gzeindakwnbruogdu","thftxvteggrtmylrx"]))