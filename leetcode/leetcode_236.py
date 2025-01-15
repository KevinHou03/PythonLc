# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        def traverse(node):
            if not node:
                return
            if node.val == p.val or node.val == q.val:
                return node
            if traverse(node.left) and traverse(node.right):
                return node
            return traverse(node.left) if traverse(node.left) else traverse(node.right)

        return traverse(root)




