class Solution(object):
    def findWords(self, words):
        rows = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
        result = []
        for word in words:
            w = word.lower()
            row = 0
            for i in range(3):
                if w[0] in rows[i]:
                    row = i
                    break
            flag = 1
            for c in w:
                if c not in rows[row]:
                    flag = 0
                    break
            if flag:
                result.append(word)
        return result