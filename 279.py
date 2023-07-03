# Perfect Squares
from collections import defaultdict, deque
class Solution(object):
    def numSquares(self, n):
        squares = []
        for i in range(101): squares.append(i ** 2)

        visited = defaultdict(bool)
        queue = deque()
        queue.append((n, 0))
        visited[n] = 1
        while queue:
            cur, steps = queue.popleft()
            if not cur: return steps
            for s in squares:
                if cur < s: break
                elif not visited[cur - s]: 
                    queue.append((cur - s, steps + 1))
                    visited[cur - s] = 1