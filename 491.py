class Solution(object):
    def findSubsequences(self, nums):
        sequences = set()
        def solve(i, seq):
            if len(seq) > 1: sequences.add(tuple(seq))
            if i == len(nums): return
            if not seq or nums[i] >= seq[-1]: solve(i + 1, seq + [nums[i]])
            solve(i + 1, seq)
        solve(0, [])
        return sequences