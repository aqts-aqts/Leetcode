class Solution(object):
    def countDigitOne(self, n):
        n = str(n)
        v = [0, 1, 20, 300, 4000, 50000, 600000, 7000000, 80000000, 900000000]
        digits = 0
        for i in range(len(n)):
            d = len(n) - i
            if d == 1: digits += 0 if n[i] == '0' else 1
            else: digits += v[d - 1] * int(n[i]) + (0 if n[i] == '0' else int(n[i + 1:]) + 1 if n[i] == '1' else int('1' + '0' * (d - 1)))
        return digits