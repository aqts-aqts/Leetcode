from math import sqrt

class Solution(object):
    def isThree(self, n):
        a = set()
        a.add(n)
        for i in range(1, int(sqrt(n)) + 1):
            if n % i == 0:
                a.add(i)
                a.add(n // i)
        return len(a) == 3