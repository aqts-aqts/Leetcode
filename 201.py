# Bitwise AND of Numbers Range
class Solution:
    def rangeBitwiseAnd(self, left, right):
        R = str(bin(right))[2:][::-1]
        D = right - left
        result = [0] * len(R)
        for i in range(len(R)):
            if int(R[i]):
                num = int(R[:i + 1][::-1], 2)
                if D <= num - 2 ** i: 
                    result[len(R) - 1 - i] = 1
        return int(''.join(map(str, result)), 2)