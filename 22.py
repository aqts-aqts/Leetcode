# Generate Parentheses
def valid(s):
    stack = []
    for c in s:
        if c == '(': stack.append(1)
        else:
            try: stack.pop()
            except: return False
    if not stack: return True
    return False

parentheses = []
def solve(n, s, open, close):
    if open == n and close == n:
        if valid(s): 
            parentheses.append(s)
            return
    if open > n or close > n: return
    solve(n, s + ')', open, close + 1)
    solve(n, s + '(', open + 1, close)

class Solution(object):
    def generateParenthesis(self, n):
        global parentheses
        parentheses = []
        solve(n, '(', 1, 0)
        return parentheses