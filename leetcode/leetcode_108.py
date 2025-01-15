class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """

        def BST(li):
            if not li:
                return
            root_index = len(li) // 2
            root = TreeNode(li[root_index])
            root.left = BST(li[:root_index])
            root.right = BST(li[root_index + 1:])
            return root
        return BST(nums)

