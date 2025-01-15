# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        result = []

        def traversal(node):
            if not node:
                return
            traversal(node.left)
            traversal(node.right)
            result.append(node.val)

        traversal(root)
        return result
