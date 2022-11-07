# Sum of Digits in Base K
class Solution:
    def sumBase(self, n, k):
        def numToBase(num, b):
            if num == 0: return [0]
            digits = []
            while num:
                digits.append(int(num % b))
                num //= b
            return digits[::-1]
        print(numToBase(n, k))
        return sum(numToBase(n, k))