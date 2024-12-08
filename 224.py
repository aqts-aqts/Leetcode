class Solution(object):
    def calculate(self, s):
        num = 0
        sign = 1
        stack = [0]
        for c in s:
            if c == ' ': continue
            if c.isdigit():
                num *= 10
                num += int(c)
            elif c == '+':
                stack[-1] += num * sign
                sign = 1
                num = 0
            elif c == '-':
                stack[-1] += num * sign
                sign = -1
                num = 0
            elif c == '(':
                stack.append(sign)
                stack.append(0)
                sign = 1
                num = 0
            else:
                n = (stack.pop() + num * sign) * stack.pop()
                stack[-1] += n
                sign = 1
                num = 0
        return stack[-1] + num * sign