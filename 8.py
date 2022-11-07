# String to Integer (atoi)
class Solution(object):
    def myAtoi(self, s):
        s = s.strip()
        if not s: return 0
        sign = 1 if s[0] == '+' else -1 if s[0] == '-' else 1
        if s[0] in '+-': s = s[1:]
        num = ''
        for c in s:
            if c not in '1234567890': break
            else: num += c
        if not num: return 0
        num = int(num) * sign
        if num > 2147483647: return 2147483647
        if num < -2147483648: return -2147483648
        return num