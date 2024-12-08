class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        # Observation: We only need to track whether the current sum is even or odd. If it is even, then it can essentially be reset to 0. Otherwise, it can essentially be reset to 1.
        # Observation 2: The value of the array elements do not matter. Only if it is even or odd.
        # Let dp[i] be the number of subarrays with an odd sum with arr[i:] that INCLUDE arr[i]
        # Observation 3: dp[i] = dp[i + 1] * 2 if arr[i] is even, otherwise, dp[i] = ((n - i) - dp[i + 1]) * 2 + 1
        # The answer is sum(dp)

        mod = 10**9 + 7
        n = len(arr)
        
        dp = [0] * n
        dp[n - 1] = arr[n - 1] % 2
        for i in range(n - 2, -1, -1):
            length = n - i
            if arr[i] % 2:
                dp[i] = length - dp[i + 1]
            else:
                dp[i] = dp[i + 1]
        
        return sum(dp) % mod