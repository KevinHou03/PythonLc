class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def bst(node):
            if not node:
                return 0
            if not node.left:
                return 1 + bst(node.right)
            if not node.right:
                return 1 + bst(node.left)
            min_h = 1 + min(bst(node.left), bst(node.right))
            return min_h

        return bst(root)


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(Solution().minDepth(root))