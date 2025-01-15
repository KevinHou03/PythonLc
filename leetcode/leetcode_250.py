# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countUnivalSubtrees(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        ans = [0]

        def dfs(node):
            if not node:
                return float("inf")
            left = dfs(node.left)
            right = dfs(node.right)
            if (left == float("inf") or left == node.val) and (right == float("inf") or right == node.val):
                ans[0] += 1
            return node.val

        dfs(root)
        return ans[0]

