# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head):
        tortoise = head
        hare = head

        while hare and hare.next:
            hare = hare.next.next
            tortoise = tortoise.next

            if hare == tortoise:
                break
        
        if not hare or not hare.next:
            return None
        
        tortoise = head
        while tortoise != hare:
            tortoise = tortoise.next
            hare = hare.next
        return tortoise