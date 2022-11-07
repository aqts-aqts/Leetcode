# Reverse Integer
class Solution(object):
    def reverse(self, x):
        x = str(x)[::-1]
        if x[-1] == '-': 
            sign = 0
            x = x[:len(x) - 1]
        else: sign = 1
        if sign:
            if int(x) > 2147483647: return 0
        else:
            if int(x) > 2147483648: return 0
        if not sign: return int(x) * -1
        else: return int(x)