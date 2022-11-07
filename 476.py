# Number Complement
class Solution:
    def findComplement(self, num):
        a = bin(num)
        a = str(a)[2:]
        t = ''
        for s in a: 
            if s == '0': t += '1'
            else: t += '0'
        return int(t, 2)