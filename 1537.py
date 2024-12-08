import copy

class Solution:
    def maxSum(self, nums1, nums2):
        C = [{}, {}]
        for i, num in enumerate(nums1):
            C[0][num] = i
        for i, num in enumerate(nums2):
            C[1][num] = i
        temp = copy.deepcopy(C)

        n = len(nums1)
        m = len(nums2)

        dp = [[0, 0] for i in range(max(n, m))]
        
        def solve(i, array):
            if array and i == n:
                return 0
            elif not array and i == m:
                return 0
            if dp[i][array]:
                return dp[i][array]
            num = nums1[i] if array else nums2[i]
            
            if array and num in C[1]:
                nextNum = C[1].pop(num)
                dp[i][array] = max(solve(i + 1, array) + num, solve(nextNum, 0))
            elif not array and num in C[0]:
                nextNum = C[0].pop(num)
                dp[i][array] = max(solve(i + 1, array) + num, solve(nextNum, 1))
            else:
                dp[i][array] = solve(i + 1, array) + num
            return dp[i][array]

        ans1 = solve(0, 1)
        ans2 = solve(0, 0)
        return max(ans1, ans2) % int(1e9+7)