from collections import defaultdict

class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        sums = defaultdict(int)
        for n1 in nums1:
            for n2 in nums2:
                sums[n1 + n2] += 1
        
        total = 0
        for n1 in nums3:
            for n2 in nums4:
                s = n1 + n2
                if -s in sums:
                    total += sums[-s]
        return total