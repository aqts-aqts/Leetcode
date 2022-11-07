# Binary Tree Preorder Traversal
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root):
        stack = []
        traversal = []
        node = root
        while stack or node is not None:
            if node is not None:
                stack.append(node)
                traversal.append(node.val)
                node = node.left
            else:
                node = stack.pop()
                node = node.right
        return traversal