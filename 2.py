# Add Two Numbers
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def getNumber(node):
    num = 0
    multiplier = 1
    cur = node
    while cur != None:
        num += cur.val * multiplier
        cur = cur.next
        multiplier *= 10
    return num

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        num = list(map(int, list(str(getNumber(l1) + getNumber(l2)))[::-1]))
        node = ListNode(num[0])
        cur = node
        for i in range(1, len(num)):
            next = ListNode(num[i])
            cur.next = next
            cur = next
        return node