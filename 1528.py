class Solution(object):
    def restoreString(self, s, indices):
        newString = [None] * len(s)
        for e, i in enumerate(indices):
            newString[i] = s[e]
        return ''.join(newString)