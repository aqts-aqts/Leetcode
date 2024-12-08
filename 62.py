class Solution(object):
    def uniquePaths(self, m, n):
        mi = min(m, n)
        mx = max(m, n)
        result = 1
        for i in range(mi - 1):
            result *= (mi + mx - 2 - i)
            result = result // (i + 1)
        return result