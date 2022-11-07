# Parsing A Boolean Expression
class Solution:
    def parseBoolExpr(self, expression):
        def solve(exp):
            print(exp)
            if exp == 'f': return False
            if exp == 't': return True
            
            if exp[0] == '!':
                stack = [0]
                i = 2
                while stack:
                    if exp[i] == '(': stack.append(1)
                    elif exp[i] == ')': 
                        if not stack.pop(): return not solve(exp[2:i])
                    i += 1
            elif exp[0] == '&':
                stack = [0]
                s = 2
                i = 2
                subexps = []
                while stack:
                    if exp[i] == '(': stack.append(1)
                    elif exp[i] == ')':
                        if not stack.pop():
                            subexps.append(exp[s:i])
                            return all(solve(e) for e in subexps)
                    elif exp[i] == ',' and len(stack) == 1:
                        subexps.append(exp[s:i])
                        s = i + 1
                    i += 1
            else:
                stack = [0]
                s = 2
                i = 2
                subexps = []
                while stack:
                    if exp[i] == '(': stack.append(1)
                    elif exp[i] == ')':
                        if not stack.pop():
                            subexps.append(exp[s:i])
                            return any(solve(e) for e in subexps)
                    elif exp[i] == ',' and len(stack) == 1:
                        subexps.append(exp[s:i])
                        s = i + 1
                    i += 1
        return solve(expression)