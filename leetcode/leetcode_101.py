class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def dfs(a,b):
            if a is None and b is None:
                return True
            if not a or not b:
                return False
            if a.val == b.val and dfs(a.left, b.right)  and dfs(a.right,b.left):
                return True
        return dfs(root.left,root.right)


