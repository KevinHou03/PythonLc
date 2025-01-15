# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: List[List[int]]
        """
        ans = []
        def backtrack(node, current_sum, path):
            if not node:
                return
            current_sum -= node.val
            path.append(node.val)

            if not node.left and not node.right and current_sum == 0:
                ans.append(path[:])

            backtrack(node.left, current_sum, path)
            backtrack(node.right, current_sum, path)
            path.pop()

        backtrack(root,targetSum,[])

        return ans