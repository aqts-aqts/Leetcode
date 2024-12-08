from math import sqrt
class Solution:
    def isPerfectSquare(self, num):
        return 1 if sqrt(num) == int(sqrt(num)) else 0