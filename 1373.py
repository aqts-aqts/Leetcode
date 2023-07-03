class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

# To solve this problem, we will use dynamic programming
# We will define two hash maps, one for the sum of all nodes in a subtree and one for whether a subtree is a BST
# To differentiate nodes from each other in the hash maps, we will map using the id of the node
# We have two helper functions, one to calculate the sum of all nodes in a subtree and one to check if a subtree is a BST
# To calculate the sum of all nodes in a subtree, we will use recursion
# We simply return the sum of the root, the sum of the left subtree and the sum of the right subtree
# To check if a subtree is a BST, we will use recursion as well
# This is a lot more complicated than it seems, as both subtrees being BSTs doesn't mean that the current subtree is a BST (even if root.left.val < root.val < root.right.val)
# This is because the left subtree might have a value greater than root.val and the right subtree might have a value less than root.val
# To get past this, we return a tuple of three values: whether the subtree is a BST, the min value in the subtree, and the max value in the subtree
# We can then confirm a BST with: if both subtrees are BSTs and the max value in the left subtree is less than the root and the min value in the right subtree is greater than the root
# To avoid recalculating the same subproblems, we will use memoization, which is the process of storing the results of subproblems so that we can use them later
# After each helper function call, we will store the result in the hash map with the id of the node as the key
# We can then do a simple inorder traversal of the tree and use the helper functions to find the maximum sum of a BST
# The time complexity of this is O(n²) where n is the number of nodes in the tree

class Solution:
    def __init__(self):
        self.sum = {}
        self.bst = {}

    def isBST(self, root: TreeNode):
        nodeId = id(root)
        if root is None:
            return (True, None, None)
        if nodeId in self.bst:
            return self.bst[nodeId]

        left_is_bst, left_min, left_max = self.isBST(root.left)
        right_is_bst, right_min, right_max = self.isBST(root.right)

        if left_is_bst and right_is_bst and (left_max is None or left_max < root.val) and (right_min is None or right_min > root.val):
            min_value = left_min if left_min is not None else root.val
            max_value = right_max if right_max is not None else root.val
            self.bst[nodeId] = (True, min_value, max_value)
        else:
            self.bst[nodeId] = (False, None, None)
        return self.bst[nodeId]
    
    def sumBST(self, root: TreeNode):
        nodeId = id(root)
        if root is None:
            return 0
        if nodeId in self.sum:
            return self.sum[nodeId]
        
        self.sum[nodeId] = root.val + self.sumBST(root.left) + self.sumBST(root.right)
        return self.sum[nodeId]

    def maxSumBST(self, root: TreeNode):
        stack = []
        node = root
        maxSum = 0
        while stack or node is not None:
            if node is not None:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                b = self.isBST(node)
                if b[0]:
                    maxSum = max(maxSum, self.sumBST(node))
                node = node.right
        return maxSum