
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None


class BST:
    def __init__(self, li=None):
        self.root = None
        if li:
            for val in li:
                self.insert_non_recur(val)

    def insert(self, node, val):
        root = node
        if not node:
            root = Node(val)

        elif val < node.data:
            node.left = self.insert(node.left, val)
            node.left.parent = node
        elif val > node.data:
            node.right = self.insert(node.right, val)
            node.right.parent = node
        else:
            pass  # 不重复

        return root

    def insert_non_recur(self, val):
        p = self.root
        if not self.root:  # 空树
            self.root = Node(val)
            return
        p = self.root
        while True:
            if val < p.data:
                if not p.left:
                    p.left = Node(val)
                    p.left.parent = p
                    return
                else:
                    p = p.left
            elif val > p.data:
                if not p.right:
                    p.right = Node(val)
                    p.right.parent = p
                    return
                else:
                    p = p.right

    # 删除有三种情况，1 删除叶子结点 2 他只有一个孩子 3 他有两个孩子 -> 拿右最小或者左最大代替他
    def find(self, node, val):
        if not node:
            return None
        elif node.data < val:
            return self.find(node.right, val)
        elif node.data > val:
            return self.find(node.left, val)
        else:
            return node

    def find_non_recur(self, val):
        p = self.root
        while p:
            if p.data < val:
                p = p.right
            elif p.data > val:
                p = p.left
            else:
                return p

        return None  # 找不到

    def __remove_node_1(self, node):  # 情况1： 叶子节点删除
        if not node.parent:  # node is the root
            self.root = None
        if node == node.parent.left:
            node.parent.left = None
        else:
            node.parent.right = None

    def __remove_node_2_left(self, node):  # 情况2：有一个左孩子
        if not node.parent:  # if it is the root
            self.root = node.left
            node.left.parent = None  # 他是根了，所以他的父亲为空了
        elif node == node.parent.left:
            node.parent.left = node.left
            node.left.parent = node.parent
        else:
            node.parent.right = node.left
            node.left.parent = node.parent

    def __remove_node_2_right(self, node):
        if not node.parent:  # it is root
            self.root = node.right
            node.right.parent = None
        elif node == node.parent.left:
            node.parent.left = node.right
            node.right.parent = node.parent
        else:
            node.parent.right = node.right
            node.right.parent = node.parent

    def delete(self, val):
        if self.root:  # 判断非空
            # 先找到value是val的这个结点
            node = self.find_non_recur(val)
            if not node:  # 能找到这个node
                return False
            if not node.left and not node.right:
                self.__remove_node_1(node)
            elif not node.right:
                self.__remove_node_2_left(node)
            elif not node.left:
                self.__remove_node_2_right(node)
            else:  # 有两个孩子
                # 找 right's min
                min_node = node.right
                while min_node.left:
                    min_node = min_node.left
                    # 现在min node在右子树最小结点处
                node.data = min_node.data  # 用min node替换被删除的节点
                if min_node.right:
                    self.__remove_node_2_right(min_node)
                else:
                    self.__remove_node_1(min_node)




def mid_order_trav(root):
    if root:
        mid_order_trav(root.left)
        print(root.data, end='')
        mid_order_trav(root.right)


tree = BST([4, 6, 7, 9, 2, 1, 3, 5, 8])
print(tree.root.data)
mid_order_trav(tree.root)  # 123456789 中序遍历会自动sort
