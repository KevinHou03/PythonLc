class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[str]
        """
        ans = []
        def track(node,path):
            path.append(node.val)
            if not node.left and not node.right:
                ans.append(path[:])
            else:
                if node.left:
                    track(node.left,path)
                if node.right:
                    track(node.right,path)
            path.pop()

        track(root,[])
        return ans

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(5)

solution = Solution()

print(solution.binaryTreePaths(root))