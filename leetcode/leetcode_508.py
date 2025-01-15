# Definition for a binary tree node.
from collections import Counter


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def findFrequentTreeSum(root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """

        ans = []
        def find_sum(node):
            if not node:
                return 0
            left_sum = find_sum(node.left)
            right_sum = find_sum(node.right)
            sum = left_sum + right_sum + node.val
            ans.append(sum)
            return sum
        find_sum(root)
        counter = Counter(ans)
        max_count = max(counter.values())
        ans = [item for item, val in counter.items() if val == max_count]
        print(counter)
        return ans

root = TreeNode(5)
root.left = TreeNode(2)
root.right = TreeNode(-5)

print(Solution.findFrequentTreeSum(root))