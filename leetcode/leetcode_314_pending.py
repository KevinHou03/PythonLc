# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """

        grid = [[]] * 200
        grid[100].append(root.val)
        left_pos = 100
        right_pos = 100
        q = deque()
        q.append(root)
        while q:
            cur = q.popleft()
            if cur.left:
                q.append(cur.left)
                grid[left_pos - 1].append(cur.left.val)
            if cur.right:
                q.append(cur.right)
                grid[right_pos + 1].append(cur.right.val)




