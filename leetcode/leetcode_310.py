from collections import defaultdict


class Solution(object):
    def findMinHeightTrees(n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """

        '''
        任何一棵树的高度都是根节点到离他最远的叶子节点的距离
        所以，如果我们能找到根节点到离他最远的叶子节点的中间那个节点，这就是MHT的根节点
        算法：不断删除叶子节点，直到剩余节点数量<2,相当于从最外层开始逐层剥离这个数，直到 n < 2
        '''
        if n == 1:
            return [0]

        # build adj list
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        # build a list of leaf node
        leaves = [i for i in range(n) if len(graph[i]) == 1]
        remain_nodes = n

        # 循环删除,如果这个叶子节点删除后他的邻居也变成了叶子节点，则把
        while remain_nodes > 2:
            leaf = leaves[0]
            remain_nodes -= len(leaves)
            new_leaves = []

            for leaf in leaves:
                neighbor = graph[leaf][0]
                graph[neighbor].remove(leaf)
                if len(graph[neighbor]) == 1:
                    new_leaves.append(neighbor)

            leaves = new_leaves

        return leaves

    # 不用list，用deque 然后直接pop会更好




