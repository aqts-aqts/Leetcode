# Make Array Zero by Subtracting Equal Amounts
def truemin(ns):
    m = 1e9
    f = False
    for n in ns:
        if not n: 
            f = True
            continue
        if n < m: m = n
    if f and m >= 1e8: return 0
    else: return m
        
class Solution:
    def minimumOperations(self, nums):
        cur = truemin(nums)
        operations = 0
        while cur > 0:
            for i in range(len(nums)): 
                if nums[i] > 0: nums[i] -= cur
            cur = truemin(nums)
            operations += 1
        return operations