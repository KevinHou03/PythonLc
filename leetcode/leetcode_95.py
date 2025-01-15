class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def generateTrees(n):
    """
    :type n: int
    :rtype: List[TreeNode]
    """
    def generate(left, right):
        if left == right: # only one node
            return [TreeNode(left)]
        if left > right:
            return [None]

        res = []
        for val in range(left, right + 1):
            root = TreeNode(val)
            for leftTree in generate(left, val - 1):# building left sub tree
                for rightTree in generate(val + 1, right):
                    root = TreeNode(val, leftTree, rightTree)
                    res.append(root)
        return res

    return generate(1, n)

print(generateTrees(3))