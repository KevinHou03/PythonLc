class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        temp = []

        def inorder_trav(node):
            if not node:
                return
            inorder_trav(node.left)
            temp.append(node)
            inorder_trav(node.right)

        inorder_trav(root)

        print(temp)

        srt_temp = sorted(n.val for n in temp)
        print(srt_temp)

        for i in range(len(srt_temp)):
            temp[i].val = srt_temp[i]

    def recoverTree2(self, root):
        '''
        在正常的二叉搜索树（BST）中，通过中序遍历（左 - 根 - 右）得到的节点值序列应该是升序的。这意味着在遍历过程中，
        任何给定节点的前一个节点的值应该小于或等于当前节点的值。
        '''
        self.first = None
        self.second = None
        self.prev = None  # 统一使用self.prev作为前一个节点的变量

        def inorder_trav(node):
            if not node:  # 如果当前节点为空，返回上一层
                return

            inorder_trav(node.left)  # 先遍历左子树

            # 如果存在前一个节点，且前一个节点的值大于当前节点的值，说明找到了一个错误顺序
            if self.prev and self.prev.val > node.val:
                if not self.first:  # 如果这是第一个找到的错误节点
                    self.first = self.prev  # 标记为first
                # 对于第二个错误节点，它可能是当前节点，也可能是后面的节点，因此每次都更新second
                self.second = node

            self.prev = node  # 更新前一个节点为当前节点

            inorder_trav(node.right)  # 再遍历右子树

        inorder_trav(root)  # 从根节点开始进行中序遍历

        # 交换第一个和第二个错误节点的值，以恢复二叉搜索树的正确顺序
        if self.first and self.second:
            self.first.val, self.second.val = self.second.val, self.first.val


root = TreeNode(2)
root.left = TreeNode(-1)
root.right = TreeNode(4)
root.right.left = TreeNode(3)
root.right.right = TreeNode(6)

Solution().recoverTree2(root)

