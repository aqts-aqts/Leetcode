import math
from collections import defaultdict

class Solution:
    def __init__(self):
        self.dp: dict[int, int] = {}
        self.primedp: dict[int, bool] = {}
        self.graph: dict[int, list[int]] = defaultdict(list)

    def isPrime(self, num: int) -> bool:
        if num == 1:
            return False
        elif num in self.primedp:
            return self.primedp[num]

        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                self.primedp[num] = False
                return False
        self.primedp[num] = True
        return True
    
    def countPaths(self, n: int, edges: list[list[int]]) -> int:
        for edge in edges:
            self.graph[edge[0]].append(edge[1])
        x = sum(self._countPaths(i, True, False) for i in range(1, n + 1))
        print(self.graph)
        print(self.dp)
        return x
        
    def _countPaths(self, i: int, first: bool, prime: bool) -> int:
        if i in self.dp:
            return self.dp[i]
        isPrime = self.isPrime(i)
        
        if not self.graph[i] and first:
            return False
        if prime and isPrime:
            return False
        prime = isPrime if not prime else prime

        paths = 0
        for neighbour in self.graph[i]:
            paths += self._countPaths(neighbour, False, prime)
        self.dp[i] = paths + int(prime)
        return self.dp[i]