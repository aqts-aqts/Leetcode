# Binary Tree Inorder Traversal
class Solution:
    def inorderTraversal(self, root):
        stack = []
        traversal = []
        node = root
        while stack or node is not None:
            if node is not None:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                traversal.append(node.val)
                node = node.right
        return traversal