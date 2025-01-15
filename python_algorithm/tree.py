
class Node:
    def __init__(self, name, type = 'dir'):
        self.name = name
        self.type = type
        self.children = []
        self.parent = None

# n1 = Node("hello")
# n2 = Node("world")
# n1.children = n2
# n2.parent = n1

class File_system_tree:
    def __init__(self):
        self.root = Node("/")

        

