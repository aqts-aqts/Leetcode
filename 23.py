import sys

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeKLists(self, lists):
        k = len(lists)
        nodes = [node for node in lists]
        root = None
        tail = None
        n = k
        while n > 0:
            minVal = sys.maxsize
            minI = -1
            for i in range(k):
                if nodes[i] is None:
                    continue
                if nodes[i].val < minVal:
                    minVal = nodes[i].val
                    minI = i
            if minI < 0:
                break
            if root is None:
                root = ListNode(minVal)
                tail = root
            else:
                tail.next = ListNode(minVal)
                tail = tail.next
                
            nodes[minI] = nodes[minI].next
            if nodes[minI] is None:
                n -= 1
        return root