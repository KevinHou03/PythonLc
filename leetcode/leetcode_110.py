# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def bst(node):
            if not node:
                return 0
            left_h = bst(node.left)
            if left_h == -1:
                return -1

            right_h = bst(node.right)
            if right_h == -1:
                return -1

            if abs(left_h - right_h) > 1:
                return -1

            return 1 + max(right_h, left_h)

        return bst(root) != -1
