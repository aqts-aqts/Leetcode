# Integer to Roman
class Solution(object):
    def intToRoman(self, num):
        roman = ['I','IV','V','IX','X','XL','L','XC','C','CD','D','CM','M']
        vals = [1,4,5,9,10,40,50,90,100,400,500,900,1000]
        n = ''
        for i in range(len(vals) - 1, -1, -1):
            if num >= vals[i]: 
                n += roman[i] * (num // vals[i])
                num -= vals[i] * (num // vals[i])
        return n