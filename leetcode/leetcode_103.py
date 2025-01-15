import collections


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        Answer = []
        queue = collections.deque() # how to declare a queue in Python
        queue.append(root)
        flag = True
        while len(queue) != 0:
            temp = []
            length = len(queue)
            for i in range(length):
                node = queue.popleft()
                if node:
                    if flag:
                        temp.append(node.val)
                    if not flag:
                        temp.insert(0,node.val)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
            flag = not flag
            if temp:
                Answer.append(temp)
        return Answer

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.right.right = TreeNode(5)

print(Solution().zigzagLevelOrder(root))

