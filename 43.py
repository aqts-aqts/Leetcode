class Solution(object):
    def multiply(self, num1, num2):
        prod = 0
        n1 = len(num1)
        n2 = len(num2)
        for i, n in enumerate(num1):
            for j, m in enumerate(num2):
                prod += int(n + '0' * (n1 - i - 1)) * int(m + '0' * (n2 - j - 1))
        return str(prod)