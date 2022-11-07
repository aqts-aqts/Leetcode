# Linked List Cycle
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head):
        if head == None: return False
        while head.next != None:
            head.val = None
            if head.next.val == None: return True
            head = head.next
        return False