from binary_search_tree import *
from python_algorithm.tree.binary_tree import *


class AVL_node(Node):
    def __init__(self, data):
        Node.__init__(self, data)
        self.balance_factor = 0


class AVL_tree(BST):
    def __init__(self, li=None):
        BST.__init__(self, li)

    def rotate_left(self, p, c):
        s2 = c.left
        p.right = s2
        if s2:  # 判断不为空
            s2.right = p
        c.left = p
        p.parent = c

        # 更新balance factor
        p.balance_factor = 0
        c.balance_factor = 0
        return c

    def rotate_right(self, p, c):
        s2 = c.right
        p.left = s2
        if s2:
            s2.parent = p
        c.right = p
        p.parent = c

        p.balance_factor = 0
        c.balance_factor = 0
        return c

    def rotate_right_left(self, p, c):
        # right rotate
        g = c.left
        s2 = g.left
        s3 = g.right
        c.left = s3
        if s3:
            s3.parent = c
        g.right = c
        c.parent = g

        # left rotate
        p.right = s2
        if s2:
            s2.parent = p
        g.left = p
        p.parent = g

        # if g.balance_factor > 0:
        #     p.balance_factor = -1
        #     c.balance_factor = 0
        # elif g.balance_factor < 0:
        #     p.balance_factor = 0
        #     c.balance_factor = -1
        # else:  # 插入的是g, s1234都是None
        #     p.balance_factor = 0
        #     c.balance_factor = 0

        if g.balance_factor > 0:
            c.balance_factor = 0
            p.balance_factor = -1
        else:
            p.balance_factor = 0
            c.balance_factor = 1
        g.balance_factor = 0
        return g

    def rotate_left_right(self, p, c):
        g = c.right
        s2 = g.left
        c.right = s2
        if s2:
            s2.parent = c
        g.left = c
        c.parent = g

        s3 = g.right
        p.left = s3
        if s3:
            s3.parent = p
        g.right = p
        p.parent = g

        # if g.balance_factor < 0:
        #     p.balance_factor = 1
        #     c.balance_factor = 0
        # elif g.balance_factor > 0:
        #     p.balance_factor = 0
        #     c.balance_factor = -1
        # else:  # 插入的是g, s1234都是None
        #     p.balance_factor = 0
        #     c.balance_factor = 0

        if g.balance_factor < 0:
            c.balance_factor = 0
            p.balance_factor = 1
        else:
            p.balance_factor = 0
            c.balance_factor = -1
        g.balance_factor = 0
        return g

    def insert_non_rec(self, val):  # 如何在插入是保持平衡
        # 先把node插进来
        p = self.root
        if not self.root:  # 空树
            self.root = Node(val)
            return
        while True:
            if val < p.data:
                if not p.left:
                    p.left = Node(val)
                    p.left.parent = p
                    node = p.left
                    # node 存的就是插入的节点
                else:
                    p = p.left
            elif val > p.data:
                if not p.right:
                    p.right = Node(val)
                    p.right.parent = p
                    node = p.right
                    # node 存的就是插入的节点
                else:
                    p = p.right
                    break
            else:  # 已经有一个这样的节点存在already exist
                return

            # 插入完毕，更新balance factor
            # 保证node的parent不是空
            while node.parent:  # 还会更新node，所以这会一直追溯到root
                if node.parent.left == node:  # 是左子，bf - 1
                    if node.parent.balance_factor < 0:  # node 的 parent -1 ---> -2
                        g = node.parent.parent  # 为了连接旋转之后的子树
                        if node.balance_factor > 0:
                            n = self.rotate_left_right(node.parent, node)
                        else:  # 是右子 bf + 1
                            n = self.rotate_right(node.parent, node)
                        # n 和 g 连起来
                    elif node.parent.balance_factor > 0:  # node 的 parent 1 ---> 0
                        node.parent.balance_factor = 0
                        break  # 为 0 就不用动了
                    else:  # node 的 parent 本来就是0 ---> -1
                        node.parent.balance_factor = -1
                        node = node.parent
                        continue
                else:  # # 是右子，bf + 1
                    if node.parent.balance_factor > 0:  # 1 ---> 2 要旋转，看哪边更沉
                        g = node.parent.parent
                        if node.balance_factor < 0:  # 左边沉
                            n = self.rotate_right_left(node.parent, node)
                        else:  # node.bf = -1
                            n = self.rotate_left(node.parent, node)
                        # 记得连g和n
                    elif node.parent.balance_factor < 0:  # node.parent -1 ---> 0
                        node.parent.balance_factor = 0
                        break
                    else:  # node.parent 0 ---> 1
                        node.parent.balance_factor = 1
                        node = node.parent
                        continue
                        # 就是说如果node parent由0 到 1了，就不用旋转，往上传

                # 现在连g和n 还是在while里面
                n.parent = g
                if g:  # g is not empty,
                    if node.parent == g.left:
                        g.left = n
                    else:
                        g.right = n
                    break
                else:  # g is empty
                    self.root = n
                    break

    def pre_order(self, root):
        if root:
            print(root.data, end='')
            pre_order(root.left)
            pre_order(root.right)

    def mid_order(self,root):
        if root:
            mid_order(root.left)
            print(root.data, end='')
            mid_order(root.right)

    def post_order(self,root):
        if root:
            post_order(root.left)
            post_order(root.right)
            print(root.data, end='')


tree = AVL_tree([9, 8, 7, 6, 5, 4, 3, 2, 1])
print("")
tree.post_order(tree.root)
