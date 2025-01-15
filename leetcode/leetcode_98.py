class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def check(self, root, lower=float('-inf'), upper=float('inf')):
        if root is None:
            return True
        if not (lower < root.val < upper):
            return False
        return self.check(root.left, lower, root.val) and self.check(root.right, root.val, upper)

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.check(root)
