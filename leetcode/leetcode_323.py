from collections import defaultdict


def countComponents(n, edges):
    """
    :type n: int
    :type edges: List[List[int]]
    :rtype: int
    """

    #首先写一个dfs，从一个点开始把所有和他connected都加到visited里面，这里面最多有一个component

    adj = defaultdict(list)
    visited = set()
    components = 0


    #无向图 两边都要
    for i, j in range(n):
        adj[i].append(j)
        adj[j].append(i)

    def dfs(node): # 递归找到所有与这个node相连的neighbor,把这些neighbor加到visited中
        visited.add(node)
        for neighbor in adj[node]:
            if neighbor not in visited:
                dfs(neighbor)


    for i in range(n):
        if i not in visited:
            components += 1
            dfs(i)
    return components




