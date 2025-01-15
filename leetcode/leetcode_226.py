# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """

        def invert(node):
            temp = node.left
            node.left = node.right
            node.right = temp

        def populate(node):
            if not node:
                return
            invert(node)
            populate(node.left)
            populate(node.right)

        populate(root)
        return root


