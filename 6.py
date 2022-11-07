# Zigzag Conversion
class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1: return s
        rows = [[] for _ in range(numRows)]
        position = 0
        direction = 1
        for i in range(len(s)):
            rows[position].append(s[i])
            position += direction
            if position == numRows - 1 or position == 0: direction *= -1
        string = ''
        for row in rows:
            string += ''.join(row)
        return string