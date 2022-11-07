# Happy Number
class Solution:
    def isHappy(self, n):
        visited = dict()
        while True:
            n = sum(map(lambda x: int(x) ** 2, str(n)))
            if n == 1: return True
            if n in visited: return False
            visited[n] = 1