def validTree(n, edges):
    """
    :type n: int
    :type edges: List[List[int]]
    :rtype: bool
    """
    if n == 0:
        return True

    # adjacency list using dict
    adj = {i : [] for i in range(n)}
    for n1, n2 in edges:
        adj[n1].append(n2)
        adj[n2].append(n1)

    visit = set()
    def dfs(i, prev): # prev标记之前的node，就是父节点，如果不这么做的话，对每个node dfs的时候可能会找到他的father去，出发cycle alert
        if i in visit:
            return False # cycle

        visit.add(i)
        for neighbor in adj[i]:
            if neighbor == prev:
                continue
            if not dfs(neighbor, i): #如果对他的neighbor们有一个返回false了，证明有循环，直接false
                return False

        return True

    dfs( 0 ,-1) and len(visit) == n

