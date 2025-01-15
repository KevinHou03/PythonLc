# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def pre_order(self,root):
        pass
    def flatten(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        """
        def dfs(root): # return the tail node of the list
            if not root:
                return None
            left_tail = dfs(root.left)
            right_tail = dfs(root.right)
            if root.left:
                left_tail.right = root.right
                root.right = root.left
                root.left = None

            return right_tail or left_tail or root # return 从左到右第一个不为none的



        dfs(root)

