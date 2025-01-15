# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections


class Solution(object):
    def findLeaves(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """

        res = collections.defaultdict(list)

        def dfs(node, layer):
            if not node:
                return layer
            # perform postorder traversal, the only one that reaches the leaf node first then the root node
            left = dfs(node.left, layer)
            right = dfs(node.right, layer)

            layer = max(left, right)
            res[layer].append(node.val)
            return layer + 1

        dfs(root, 0)
        return res.values()