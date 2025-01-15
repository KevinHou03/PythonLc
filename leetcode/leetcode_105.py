'''
1. the first value in PRE-order is always the root
2. 所以，可以recursively从preorder中弹出最左边的元素，剩下的最左边的就是subtree的root
3. For Inorder traversal, 对于每一个从preorder弹出的元素（root）
他在inorder里面的位置的前一个元素永远是他的left node，如果inorder里面该node
的左边没有元素了，那说明他没有left sub
4. 同理，在inorder中找到该弹出的node，他的右边的元素就是他的right subtree
'''

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder[0])
        index = inorder.indexOf(preorder[0])
        root.left = self.buildTree(preorder[1 : index + 1], inorder[ : index])
        root.right = self.buildTree(preorder[index + 1 : ], inorder[index + 1: ])

        return root




