class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self, val):
        if not self.root:
            self.root = TreeNode(val)
            self.size += 1
        else:
            self.root = self._insert(self.root, val)

    def _insert(self, root, val):
        if not root:
            self.size += 1
            return TreeNode(val)
        elif val < root.val:
            root.left = self._insert(root.left, val)
        else:
            root.right = self._insert(root.right, val)
        
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
        balance = self.getBalance(root)

        if balance > 1 and val < root.left.val:
            if val < root.left.val:
                return self.rightRotate(root)
            else:
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)
        
        if balance < -1 and val > root.right.val:
            if val > root.right.val:
                return self.leftRotate(root)
            else:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)
        return root
    
    def delete(self, val):
        if not self.root:
            return
        self.root = self._delete(self.root, val)

    def _delete(self, root, val):
        if not root:
            return root
        elif val < root.val:
            root.left = self._delete(root.left, val)
        elif val > root.val:
            root.right = self._delete(root.right, val)
        else:
            if not root.left:
                temp = root.right
                root = None
                self.size -= 1
                return temp
            elif not root.right:
                temp = root.left
                root = None
                self.size -= 1
                return temp
            temp = self.getMinValueNode(root.right)
            root.val = temp.val
            root.right = self._delete(root.right, temp.val)

        if not root:
            return root
        
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
        balance = self.getBalance(root)

        if balance > 1 and self.getBalance(root.left) >= 0:
            return self.rightRotate(root)
        if balance < -1 and self.getBalance(root.right) <= 0:
            return self.leftRotate(root)
        if balance > 1 and self.getBalance(root.left) < 0:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
        if balance < -1 and self.getBalance(root.right) > 0:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)
        return root
    
    def contains(self, val):
        return self._contains(self.root, val)
    
    def _contains(self, root, val):
        if not root:
            return False
        elif val < root.val:
            return self._contains(root.left, val)
        elif val > root.val:
            return self._contains(root.right, val)
        else:
            return True
        
    def search(self, low, high):
        return self._search(self.root, low, high)
    
    def _search(self, root, low, high):
        if not root:
            return False
        elif root.val >= low and root.val <= high:
            return True
        elif root.val < low:
            return self._search(root.right, low, high)
        else:
            return self._search(root.left, low, high)
    
    def leftRotate(self, node):
        right = node.right
        rightLeft = right.left
        right.left = node
        node.right = rightLeft
        node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))
        right.height = 1 + max(self.getHeight(right.left), self.getHeight(right.right))
        return right
    
    def rightRotate(self, node):
        left = node.left
        leftRight = left.right
        left.right = node
        node.left = leftRight
        node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))
        left.height = 1 + max(self.getHeight(left.left), self.getHeight(left.right))
        return left
    
    def getHeight(self, node):
        if not node:
            return 0
        return node.height
    
    def getBalance(self, node):
        if not node:
            return 0
        return self.getHeight(node.left) - self.getHeight(node.right)
    
    def getMinValueNode(self, node):
        if node is None or node.left is None:
            return node
        return self.getMinValueNode(node.left)

    def __len__(self):
        return self.size

class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, indexDiff, valueDiff):
        # To solve this problem, we will use a sliding window and a balanced binary search tree to optimize searching, insertion and deletion
        # For each iteration, we will check if the current element is within valueDiff of any element in the tree
        # If there is, we return True, otherwise we insert the current element into the tree
        # If the size of the tree is greater than indexDiff, we delete the element that is indexDiff away from the current element
        # The time complexity of this is O(nlogk) where n is the number of elements in the array and k is the indexDiff
        # The space complexity is O(k) where k is the indexDiff

        n = len(nums)
        tree = AVLTree()

        for i in range(n):
            if tree.search(nums[i] - valueDiff, nums[i] + valueDiff):
                return True
            tree.insert(nums[i])
            if len(tree) > indexDiff:
                tree.delete(nums[i - indexDiff])
        return False