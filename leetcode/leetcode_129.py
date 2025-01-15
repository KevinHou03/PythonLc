# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        result = []
        def dfs(cur, path):
            if not cur:
                return
            path.append(cur.val)
            if not cur.left and not cur.right:
                result.append("".join(map(str, path)))
            else:
                if cur.left:
                    dfs(cur.left, path)
                if cur.right:
                    dfs(cur.right, path)
            path.pop()

        dfs(root, [])
        return sum(int(num) for num in result)


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print(Solution().sumNumbers(root))

