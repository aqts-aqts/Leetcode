class Solution(object):
    def combinationSum(self, nums, target):
        combos = set()
        def solve(n, i, path = None):
            if path is None: path = []
            if n == target: combos.add(tuple(path))
            elif n > target: return

            solve(n + nums[i], i, path + [nums[i]])
            if i + 1 < len(nums): 
                solve(n, i + 1, path)
        solve(0, 0)
        return combos