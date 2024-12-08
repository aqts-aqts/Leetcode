import time
class Solution(object):
    def combinationSum2(self, nums, target):
        combos = set()
        h = dict()
        for num in nums:
            if num in h: h[num] += 1
            else: h[num] = 1
        nums = sorted(list(set(nums)))

        def solve(n, i, freq, path = None):
            if path is None: path = []
            if n == target: combos.add(tuple(sorted(path)))
            elif n > target: return
            
            if freq[nums[i]] > 0:
                freq[nums[i]] -= 1
                solve(n + nums[i], i, freq.copy(), path + [nums[i]])

            if i + 1 < len(nums): solve(n, i + 1, freq.copy(), path)
            else:
                if n + nums[i] == target and freq[nums[i]] > 0: combos.add(tuple(sorted(path + [nums[i]])))
        solve(0, 0, h.copy())
        return combos