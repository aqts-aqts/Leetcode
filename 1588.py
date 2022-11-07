# Sum of All Odd Length Subarrays
class Solution:
    def sumOddLengthSubarrays(self, arr):
        n = len(arr)
        l = 1
        total = 0
        while n >= l:
            subsum = sum(arr[:l])
            total += subsum
            for i in range(n - l):
                subsum -= arr[i]
                subsum += arr[i + l]
                total += subsum
            l += 2
        return total