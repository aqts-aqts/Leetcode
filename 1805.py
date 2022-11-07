# Number of Different Integers in a String
class Solution:
    def numDifferentIntegers(self, word):
        nMap = {}
        n = 0
        cur = ''
        for i, c in enumerate(word):
            if c in '1234567890': cur += c
            elif cur:
                num = int(cur)
                cur = ''
                if num in nMap: continue
                nMap[num] = 1
                n += 1
        if cur and int(cur) not in nMap: n += 1
        print(nMap)
        return n