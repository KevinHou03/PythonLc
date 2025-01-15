# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def largestBSTSubtree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0
        self.max_val = 1
        self.dfs(root)
        return self.max_val

    #  (is it a bst, size of the bst, min_val, max_val)
    def dfs(self, node):
        if not node:
            return (False, 0, -10001, 10001)
        if not node.left and not node.right: # leaf node
            return (True, 1, node.val, node.val)
        l_isBST, l_size, l_min, l_max = self.dfs(node.left)
        r_isBST, r_size, r_min, r_max = self.dfs(node.right)

        if l_isBST and r_isBST and l_max < node.val < r_min:
            size = 1 + l_size + r_size
            self.max_val = max(self.max_val, size)
            return (True, size, l_min, r_max)
        elif l_isBST and not node.right and l_max < node.val:
            size = 1 + l_size
            self.max_val = max(self.max_val, size)
            return (True, size, l_min, node.val)
        elif r_isBST and not node.left and r_min > node.val:
            size = 1 + r_size
            self.max_val = max(self.max_val, size)
            return (True, size, node.val, r_max)
        else:
            return (False, 0, -10001, 10001)







