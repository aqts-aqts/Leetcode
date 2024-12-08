class Solution:
    def getMinSum(self, n):
        if n % 3 == 0:
            return n // 3
        return (n - n % 3) // 3 + 1

    def minimumRounds(self, tasks: list[int]) -> int:
        t = {}
        for task in tasks:
            if task not in t:
                t[task] = 1
            else:
                t[task] += 1
        n = len(t)
        rounds = 0
        for task in t:
            if t[task] > 1:
                rounds += self.getMinSum(t[task])
            else:
                return -1
        return rounds