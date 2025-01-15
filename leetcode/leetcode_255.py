class Solution(object):
    def verifyPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        """
        def aux(left, right, min, max):
            if left > right:
                return True
            root = preorder[left]
            if root <= min or root >= max:
                return False

            #找到右子树第一个value也就是大于根节点的第一个node
            right_first = left + 1
            while left <= right and preorder[right_first] <= root:
                right_first += 1
            return aux(left + 1, right_first - 1, min, root) and aux(right_first, right, root, max)
        return aux(0, len(preorder) - 1, float("-inf"), float("inf"))

