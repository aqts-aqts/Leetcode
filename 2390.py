class Solution:
    def removeStars(self, s):
        n = len(s)
        stack = []
        newString = ''
        for i in range(n - 1, -1, -1):
            if s[i] == '*':
                stack.append(i)
            elif stack:
                stack.pop()
            else:
                newString = s[i] + newString
        return newString