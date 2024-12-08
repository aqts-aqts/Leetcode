# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def rangeSumBST(self, root, low, high):
        def traverse(node):
            if node is None: return 0
            return (node.val if low <= node.val <= high else 0) + traverse(node.left) + traverse(node.right)
        return traverse(root)