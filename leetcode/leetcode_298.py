# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        counter = 0

        def dfs(node, length):
            if not root:
                return
            self.max_length = max(self.max_length, length)
            if node is None:
                return
            if node.left and node.left.val == node.val + 1:
                dfs(node.left, length + 1)
            else:
                dfs(node.left, 0)
            if node.right and node.right.val == node.val + 1:
                dfs(node.right, length + 1)
            else:
                dfs(node.right, 0)

        self.max_length = 0
        dfs(root, 1)
        return self.max_length


root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)
root1.left.left = TreeNode(3)
root1.left.right = TreeNode(5)
root1.left.left.left = TreeNode(6)

print(Solution.longestConsecutive(root1,root1))