# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from leetcode.leetcode_293 import target


class Solution(object):
    def deleteNode(root, key):
        """
        :type root: Optional[TreeNode]
        :type key: int
        :rtype: Optional[TreeNode]
        """
        if not root:
            return None
        # 首先查找该node
        cur = root
        prev = root
        target_node = None
        while cur:
            if cur.val == key:
                target_node = cur
                break
            elif cur.val < key:
                prev = cur
                cur = cur.right
            else:
                prev = cur
                cur = cur.left

        # 如果找不到该node则返回空
        if not target_node:
            return None

        #情况一：叶子节点 直接remove
        if not target_node.left and not target_node.right:
            if target_node == root:
                return None
            if prev.left == target_node:
                prev.left = None
            else:
                prev.right = None

        #情况二：有一个孩子，左或者右
        elif not target_node.left or not target_node.right:
            if target_node == root:
                return target_node.right or target_node.left
            if prev.left == target_node:
                prev.left = target_node.left or target_node.right
            else:
                prev.right = target_node.right or target_node.left

        #情况三：两个子
        else:
            successor_pre = target_node
            successor = target_node.right
            while successor.left:
                successor_pre = successor
                successor = successor.left
            target_node.val = successor.val

            if successor_pre.left == successor:
                successor_pre.left = successor.right
            else:
                successor_pre.right = successor.right

        return root









