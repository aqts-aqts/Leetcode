# Remove Linked List Elements
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head, val):
        while head is not None and head.val == val: head = head.next
        if head is None: return None
        
        prev = head
        cur = head.next
        while cur is not None:
            if cur.val == val: prev.next = cur.next
            else: prev = cur
            cur = cur.next
        return head