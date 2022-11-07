# Jump Game IV
from collections import defaultdict, deque
class Solution(object):
    def minJumps(self, arr):
        map = defaultdict(list)
        for index, i in enumerate(arr):
            map[i].append(index)
        queue = deque()
        visited = [0] * len(arr)
        queue.append((0, 0))
        visited[0] = 1
        while queue:
            cur, steps = queue.popleft()
            if cur == len(arr) - 1: return steps
            while map[arr[cur]]:
                if not visited[map[arr[cur]][-1]]:
                    queue.append((map[arr[cur]][-1], steps + 1))
                    visited[map[arr[cur]][-1]] = 1
                map[arr[cur]].pop()
            if cur < len(arr) - 1 and not visited[cur + 1]: 
                queue.append((cur + 1, steps + 1))
                visited[cur + 1] = 1
            if cur > 0 and not visited[cur - 1]: 
                queue.append((cur - 1, steps + 1))
                visited[cur - 1] = 1