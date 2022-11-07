# Median of Two Sorted Arrays
from sys import maxsize
def median(l):
    if len(l) % 2 == 0: return float(l[len(l) // 2 - 1] + l[len(l) // 2]) / 2
    else: return l[len(l) / 2]

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        if len(nums1) == 0: return median(nums2)
        if len(nums2) == 0: return median(nums1)
        if len(nums1) > len(nums2): return self.findMedianSortedArrays(nums2, nums1)
        mid = (len(nums1) + len(nums2) + 1) // 2
        start = 0
        end = len(nums1)
        while start <= end:
            size1 = (start + end) // 2
            size2 = mid - (start + end) // 2
            left1 = nums1[size1 - 1] if size1 > 0 else -maxsize - 1
            left2 = nums2[size2 - 1] if size2 > 0 else -maxsize - 1
            right1 = nums1[size1] if size1 < len(nums1) else maxsize
            right2 = nums2[size2] if size2 < len(nums2) else maxsize

            if left1 > right2: end = (start + end) // 2 - 1
            elif left2 > right1: start = (start + end) // 2 + 1

            if left1 <= right2 and left2 <= right1:
                if (len(nums1) + len(nums2)) % 2 == 0: return float(max(left1, left2) + min(right1, right2)) / 2
                else: return max(left1, left2)