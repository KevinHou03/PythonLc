# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findMode(root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """

        memo = {}

        def dfs(node):
            if not node:
                return
            if node.val in memo:
                memo[node.val] += 1
            else:
                memo[node.val] = 1
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        max_count = max(memo.values())
        return [item for item, value in memo.items() if value == max_count]



