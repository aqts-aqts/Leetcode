class Solution:
    def validateStackSequences(self, pushed, popped):
        pushed = list(reversed(pushed))
        popped = list(reversed(popped))

        stack = []
        while popped:
            if not stack:
                stack.append(pushed.pop())
                
            if stack[-1] == popped[-1]:
                stack.pop()
                popped.pop()
            else:
                try:
                    stack.append(pushed.pop())
                except:
                    return False
        return True