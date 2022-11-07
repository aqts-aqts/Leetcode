# Count Subarrays With Score Less Than K
class Solution:
    def countSubarrays(self, nums, k):
        sum = 0
        product = 0
        start = 0
        end = 0
        result = 0
        while end < len(nums):
            sum += nums[end]
            product = sum * (end - start + 1)
            while start < end and product >= k:
                sum -= nums[start]
                start += 1
                product = sum * (end - start + 1)
            if product < k:
                result += end - start + 1
            end += 1
        return result