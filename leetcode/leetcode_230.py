# Definition for a binary tree node.
from inspect import stack


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        nodes = []
        def traverse(node):
            if not node:
                return
            traverse(node.left)
            nodes.append(node.val)
            traverse(node.right)

        traverse(root)
        return nodes[k - 1]


    def kthSmallest2(self, root, k):

        stack = []
        cur = root
        count = 0 # the ith time we pop = the ith smallest value

        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            count += 1
            if count == k:
                return cur.val
            cur = cur.right

