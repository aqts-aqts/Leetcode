# Jump Game III
from collections import deque
def solve(index, arr):
    visited = [0] * len(arr)
    queue = deque()
    queue.append(index)
    visited[index] = 1
    while queue:
        cur = queue.popleft()
        if arr[cur] == 0: return True
        if cur + arr[cur] < len(arr) and not visited[cur + arr[cur]]: 
            queue.append(cur + arr[cur])
            visited[cur + arr[cur]] = 1
        if cur - arr[cur] >= 0 and not visited[cur - arr[cur]]: 
            queue.append(cur - arr[cur])
            visited[cur - arr[cur]] = 1
    return False

class Solution(object):
    def canReach(self, arr, start):
        return solve(start, arr)