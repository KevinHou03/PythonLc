class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None


a = Node("A")
b = Node("B")
c = Node("C")
d = Node("D")
e = Node("E")
f = Node("F")
g = Node("G")

e.left = a
e.right = g
a.right = c
c.left = b
c.right = d
g.right = f

root = e
print(root.left.right.data)  # C


def pre_order(root):
    if root:
        print(root.data, end='')
        pre_order(root.left)
        pre_order(root.right)


def mid_order(root):
    if root:
        mid_order(root.left)
        print(root.data, end='')
        mid_order(root.right)


def post_order(root):
    if root:
        post_order(root.left)
        post_order(root.right)
        print(root.data, end='')


def traverse_tree(root):
    result = []
    queue = [root]

    while queue:
        level_node = []
        node_num = len(queue)

        for element in range(node_num):
            current_node = queue.pop(0)
            level_node.append(current_node.data)

            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
        result.append(level_node)

    return result


def traverse2(root):  # written by myself, better
    result = []
    queue = [root]

    while queue:
        node = queue.pop(0)
        result.append(node.data)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return result


print(traverse_tree(root))
traverse_tree(root)
print(traverse2(root))


