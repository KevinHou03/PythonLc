
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """

        inorder_map = {v:i for i, v in enumerate(inorder)}

        if not inorder:
            return None
        root = TreeNode(postorder.pop())
        # index = inorder.index(root.val)
        index = inorder_map[root.val]
        root.right = self.buildTree(inorder[index + 1 :],postorder[1:])
        root.left = self.buildTree(inorder[:index], postorder)
        return root