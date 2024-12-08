from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        last = None
        while node is not None:
            if last is not None and last.val == node.val:
                node = node.next
                last.next = node
            else:
                last = node
                node = node.next
        return head