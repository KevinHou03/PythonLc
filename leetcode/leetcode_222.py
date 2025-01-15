# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countNodes(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        if not root:
            return 0

        def find_depth(node):
            count = 0
            while node:
                count += 1
                node = node.left
            return count

        def bfs(node):
            if not node:
                return 0
            
            left_depth = find_depth(node.left)
            right_depth = find_depth(node.right)

            if left_depth == right_depth:
                return (2**left_depth) + bfs(node.right)
            else:
                return bfs(node.left) + bfs(node.right)

        return bfs(root)


