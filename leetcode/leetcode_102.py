import collections


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        Answer = []
        queue = collections.deque() # how to declare a queue in Python
        queue.append(root)
        while len(queue) != 0:
            temp = []
            for i in range(len(queue)):
                node = queue.popleft()
                if node:
                    temp.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if temp:
                Answer.append(temp)
        return Answer







