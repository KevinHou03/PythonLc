class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        result = []
        if root is not None:
            result += self.inorderTraversal(root.left)
            result.append(root.val)
            result += self.inorderTraversal(root.right)
        return sorted(result)

root = TreeNode(0)
root.left = TreeNode(-1)
# root.right = TreeNode(4)
# root.right.left = TreeNode(3)
# root.right.right = TreeNode(6)


print(Solution().inorderTraversal(root))



list1 = [-1,0]
print(set(list1))
