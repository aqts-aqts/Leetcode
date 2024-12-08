class Solution(object):
    def minimumPartition(self, s, k):
        cur = 0
        ss = 1
        for i, num in enumerate(s):
            next = cur * 10 + int(num)
            if next > k: 
                ss += 1 
                cur = int(num)
            else:
                cur = next
            if cur > k: return -1
        return ss