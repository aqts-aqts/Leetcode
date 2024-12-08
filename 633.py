class Solution:
    def judgeSquareSum(self, c):
        i = 0
        while True:
            dif = c - i ** 2
            if dif < 0:
                return False
            if (dif ** 0.5) % 1 == 0:
                return True
            i += 1