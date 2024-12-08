class Solution(object):
    def merge(self, nums1, m, nums2, n):
        pointer = 0
        for i in range(len(nums2)):
            while nums1[pointer]:
                pointer += 1
            nums1[pointer] = nums2[i]
            pointer += 1
        nums1.sort()