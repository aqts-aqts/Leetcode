import math

class Solution(object):
    def distinctPrimeFactors(self, nums):
        s = sum(nums)
        factors = set()
        for x in range(len(nums)):
            for i in range(2, int(math.sqrt(nums[x])) + 2):
                if (nums[x] % i == 0):
                    factors.add(i)
                    while nums[x] % i == 0: nums[x] //= i
            if nums[x] > 2: factors.add(nums[x])
        return len(factors)