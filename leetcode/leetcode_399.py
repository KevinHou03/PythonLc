from collections import defaultdict, deque


def calcEquation(equations, values, queries):
    """
    :type equations: List[List[str]]
    :type values: List[float]
    :type queries: List[List[str]]
    :rtype: List[float]
    """
    global dfs
    res = []
    graph = defaultdict(list)
    for i, eq in enumerate(equations):
        a, b = eq[0], eq[1]
        graph[a].append([b, values[i]])
        graph[b].append([a, 1 / values[i]])

        def dfs(src, target):
            if src not in graph or target not in graph:
                return -1
            q, visit = deque(), set()
            q.append([src, 1])
            visit.add(src)
            while q:
                node, val = q.popleft()
                if node == target:
                    return val
                for neighbor, val2 in graph[node]:
                    if neighbor not in visit:
                        q.append([neighbor, val * val2])
                        visit.add(neighbor)
            return -1

    for j in range(len(queries)):
        a, b = queries[j][0], queries[j][1]
        res.append(dfs(a, b))

    return res




