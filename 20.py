# Valid Parentheses
class Solution:
    def isValid(self, s):
        stack = []
        for c in s:
            if c in '({[': stack.append(c)
            elif c == ')':
                if stack and stack[-1] == '(': stack.pop()
                else: return False
            elif c == '}':
                if stack and stack[-1] == '{': stack.pop()
                else: return False
            else:
                if stack and stack[-1] == '[': stack.pop()
                else: return False
        if not stack: return True
        else: return False