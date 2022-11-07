# Find Common Characters
class Solution:
    def commonChars(self, words):
        chars = []
        for c in words[0]:
            found = True
            for i in range(1, len(words)):
                pos = words[i].find(c)
                if pos == -1:
                    found = False
                    break
                else:
                    words[i] = words[i][0:pos] + '0' + words[i][pos + 1:]
            if found:
                chars.append(c)
        return chars