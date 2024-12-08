class Solution(object):
    def findDifference(self, nums1, nums2):
        a = {}
        b = {}
        for num in nums1:
            a[num] = 1
        for num in nums2:
            b[num] = 1
        answer = [[], []]
        for num in a:
            if num not in b:
                answer[0].append(num)
        for num in b:
            if num not in a:
                answer[1].append(num)
        return answer