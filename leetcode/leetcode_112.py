# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """

        def dfs(node, cur_sum):
            if not node:
                return False
            cur_sum += node.val
            if not node.left and node.right: #加这个因为必须要检索到leaf，并且找到等于的，才能true，半途就等于了只能false
                return cur_sum == targetSum
            return dfs(node.left, cur_sum) or dfs(node.right, cur_sum)

        return dfs(root, 0)


def find_prime(a):
    for i in range(2, a + 1):
        is_prime = True
        for j in range(2, i // 2):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            print(i)


find_prime(100)

def find_prime2(a):
    for i in range(2, a + 1):  # Start loop from 2, since 1 is not a prime number
        is_prime = True
        for j in range(2, a - 1):  # Only go up to the square root of i
            if i % j == 0:
                is_prime = False
                break  # Exit the inner loop immediately if a factor is found
        if is_prime:
            print(i)

# Example usage:
find_prime2(20)
