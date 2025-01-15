# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections


class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        # base case
        if not root:
            return []

        level_dict = collections.defaultdict(list)
        res = []
        max_x = float("-inf")
        min_x = float("inf")

        # use level traversal
        q = collections.deque([(0, root)])

        while q:
            x, node = q.popleft()
            level_dict[x].append(node.val)

            min_x = min(min_x, x)
            max_x = max(max_x, x)

            if node.left:
                q.append((x - 1, node.left))
            if node.right:
                q.append((x + 1, node.right))

        for i in range(min_x, max_x + 1):
            res.append(level_dict[i])

        return res




