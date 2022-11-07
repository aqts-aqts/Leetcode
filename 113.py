# Path Sum II
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def pathSum(self, r, t):
        paths = []
        def solve(root, targetSum, path=None):
            if not root: return
            if not path: path = [root.val]
            if not root.left and not root.right: 
                if root.val == targetSum: 
                    paths.append(path)
                    return
            elif root.left and root.right: 
                solve(root.left, targetSum - root.val, path + [root.left.val])
                solve(root.right, targetSum - root.val, path + [root.right.val])
            elif root.right: solve(root.right, targetSum - root.val, path + [root.right.val])
            else: solve(root.left, targetSum - root.val, path + [root.left.val])
        solve(r, t)
        return paths