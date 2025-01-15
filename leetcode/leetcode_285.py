# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """

        if not root:
            return None

        stack = []
        res = []

        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            res.append(root)
            if len(res) > 1 and res[-2] == p:
                return res[-1]
            root = root.right

    def preorder_logic(self, root):
        if not root:
            return None

        stack, res = [], []
        while stack or root:
            while root:
                stack.append(root)
                root = root.right

            root = stack.pop()
            res.append(root.val)
            root = root.left

        return res





root1 = TreeNode(5)
root1.left = TreeNode(3)
root1.right = TreeNode(6)
root1.left.left = TreeNode(2)
root1.left.right = TreeNode(4)
root1.left.left.left = TreeNode(1)

# print(Solution().inorderSuccessor(root1, 2))
print(Solution().preorder_logic(root1))
