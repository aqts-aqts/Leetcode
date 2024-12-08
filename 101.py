from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        lstack = []
        ltraversal = []
        lnode = (root.left, -1)
        
        while lstack or lnode[0] is not None:
            if lnode[0] is not None:
                lstack.append(lnode)
                lnode = (lnode[0].left, 0)
            else:
                lnode = lstack.pop()
                ltraversal.append((lnode[0].val, lnode[1]))
                lnode = (lnode[0].right, 1)

        rstack = []
        rtraversal = []
        rnode = (root.right, -1)

        while rstack or rnode[0] is not None:
            if rnode[0] is not None:
                rstack.append(rnode)
                rnode = (rnode[0].right, 0)
            else:
                rnode = rstack.pop()
                rtraversal.append((rnode[0].val, rnode[1]))
                rnode = (rnode[0].left, 1)
        
        print(ltraversal, rtraversal)
        return ltraversal == rtraversal