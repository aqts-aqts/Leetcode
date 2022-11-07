# Roman to Integer
class Solution:
    def romanToInt(self, s):
        vals = {'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10, 'XL': 40, 'L': 50, 'XC': 90, 'C': 100, 'CD': 400, 'D': 500, 'CM': 900, 'M': 1000}
        total = 0
        i = 0
        while i < len(s):
            print(total)
            if i < len(s) - 1 and s[i] + s[i + 1] in vals: 
                total += vals[s[i] + s[i + 1]]
                i += 2
            else: 
                total += vals[s[i]]
                i += 1
        return total