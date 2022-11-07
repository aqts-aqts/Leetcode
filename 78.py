# Subsets
class Solution:
    def subsets(self, x):
        subsets = []
        if not x:
            subsets.append(x)
        else:
            A = x[0]
            B = x[1:]
            for s in self.subsets(B):
                subsets.append(s)
                result = [A] + s
                subsets.append(result)
        return subsets