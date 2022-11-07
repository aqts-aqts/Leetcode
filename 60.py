# Permutation Sequence
dp = {}
def factorial(n):
    if n < 2: return 1
    if n in dp: return dp[n]
    dp[n] = n * factorial(n - 1)
    return dp[n]

class Solution:
    def getPermutation(self, n, k):
        start = {1: [1], 2: [1, 2], 3: [1, 2, 3], 4: [1, 2, 3, 4], 5: [1, 2, 3, 4, 5], 6: [1, 2, 3, 4, 5, 6], 7: [1, 2, 3, 4, 5, 6, 7], 8: [1, 2, 3, 4, 5, 6, 7, 8], 9: [1, 2, 3, 4, 5, 6, 7, 8, 9]}
        nums = start[n]
        sequence = []
        k -= 1
        while nums:
            n -= 1
            permute = factorial(n)
            group = k // permute
            k %= permute
            sequence.append(nums.pop(group))
        return ''.join(map(str, sequence))