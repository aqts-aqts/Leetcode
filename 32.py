# Longest Valid Parentheses
class Solution:
    def longestValidParentheses(self, s):
        bracketMap = {}
        stack = []
        for i, c in enumerate(s):
            if c == '(': stack.append(i)
            else: 
                if stack: bracketMap[stack.pop()] = 1
        
        stack = []
        length = 0
        longest = 0
        for i, c in enumerate(s):
            if c == '(':
                if i not in bracketMap:
                    stack = []
                    length = 0
                else: stack.append(1)
            else:
                if stack: 
                    stack.pop()
                    length += 2
                else:
                    stack = []
                    length = 0
            longest = max(longest, length)
        return longest