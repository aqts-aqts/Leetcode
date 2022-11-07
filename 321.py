# Create Maximum Number
class Solution:
    def maxNumber(self, nums1, nums2, k):
        m = len(nums1)
        n = len(nums2)
        dp = {}
        def solve(i, j, length):
            if not length: return '' # base case
            if (i, j, length) in dp: return dp[(i, j, length)] # recall

            # greedy
            max1 = None
            max2 = None
            for k in range(i, m): # find max1
                if (m - k + n - j) < length: break # check if still able to form number with length digits
                if max1 is None or nums1[max1] < nums1[k]: max1 = k # update max value
            for k in range(j, n): # find max2
                if (m - i + n - k) < length: break
                if max2 is None or nums2[max2] < nums2[k]: max2 = k
            
            # dp
            maxNum = None
            if max1 is not None and max2 is not None:
                if nums1[max1] > nums2[max2]: maxNum = str(nums1[max1]) + solve(max1 + 1, j, length - 1) # get max from nums1
                elif nums1[max1] < nums2[max2]: maxNum = str(nums2[max2]) + solve(i, max2 + 1, length - 1) # get max from nums2
                else: maxNum = max(str(nums1[max1]) + solve(max1 + 1, j, length - 1), str(nums2[max2]) + solve(i, max2 + 1, length - 1)) # try both
            elif max1 is not None: maxNum = str(nums1[max1]) + solve(max1 + 1, j, length - 1) # nums2 empty
            elif max2 is not None: maxNum = str(nums2[max2]) + solve(i, max2 + 1, length - 1) # nums1 empty

            dp[(i, j, length)] = maxNum # memoize
            return maxNum
        solve(0, 0, k)
        return dp[(0, 0, k)]