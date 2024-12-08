# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reverseKGroup(self, head, k):
        n = 0
        node = head
        nums = []
        while node is not None:
            n += 1
            nums.append(node.val)
            node = node.next

        array = [0] * n
        cur = k
        for i in range(n):
            array[cur - 1] = nums[i]
            cur -= 1
            if cur % k == 0:
                cur += 2 * k
            if cur > n:
                cur -= k
                break
        for i in range(cur, n):
            array[i] = nums[i]

        root = ListNode(array[0])
        tail = root
        for i in range(1, n):
            tail.next = ListNode(array[i])
            tail = tail.next
        print(array)
        return root