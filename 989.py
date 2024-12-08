class Solution(object):
    def addToArrayForm(self, num, k):
        return list(map(int,list(str(sum(n*(10**(len(num)-i-1))for i, n in enumerate(num))+k))))