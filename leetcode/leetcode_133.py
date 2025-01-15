
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []



class Solution(object):
    def cloneGraph(node):
        """
        :type node: Node
        :rtype: Node
        """
        oldToNew = {}

        def dfs(node):
            if node in oldToNew: #不会有重复克隆的节点
                return oldToNew[node]
            new_node = Node(node.val) # head
            oldToNew[node] = new_node
            for neighbor in node.neighbors:
                new_node.neighbors.append(dfs(neighbor))
        dfs(node)
        return new_node

