# starting from index 0
def bellman_ford(V, E, src):
    # Step 1: 初始化距离和前驱节点数组
    distance = [float('inf')] * V
    predecessor = [-1] * V
    distance[src] = 0

    # Step 2: 松弛所有边 V-1 次
    for _ in range(V - 1):
        for u, v, weight in E:
            if distance[u] != float('inf') and distance[u] + weight < distance[v]:
                distance[v] = distance[u] + weight
                predecessor[v] = u

    # Step 3: 检测负权重环
    for u, v, weight in E:
        if distance[u] != float('inf') and distance[u] + weight < distance[v]:
            print("Graph contains negative weight cycle")
            return None, None

    return distance, predecessor

def find_path(src, target, predecessor):
    # 回溯路径
    path = []
    current = target
    while current != src:
        if current == -1:  # 如果当前节点为-1，说明路径不存在
            return []
        path.append(current)
        current = predecessor[current]
    path.append(src)
    path.reverse()  # 因为是从目标顶点回溯到源点，所以最后需要反转列表
    return path

# 示例用法
V = 7  # 顶点数（根据您的边列表调整）
E = [(0, 1, 6), (0, 2, 5), (0, 3, 5), (1, 4, -1), (2, 1, -2), (2, 4, 1), (3, 2, -2), (3, 5, -1), (4, 6, 3), (5, 6, 3)]  # 边的列表，(u, v, weight)

distance, predecessor = bellman_ford(V, E, 0)
if distance is not None:
    print("Distance from source:", distance)
    print("Predecessor in path:", predecessor)

    # 获取从源点到顶点 6 的路径
    path = find_path(0, 6, predecessor)
    print("Path to vertex 6:", path)




# starting from index 1
def bellman_ford(V, E, src):
    # Step 1: 初始化距离和前驱节点数组
    distance = [float('inf')] * (V + 1)  # 数组大小为 V + 1，因为顶点编号从 1 到 V
    predecessor = [-1] * (V + 1)
    distance[src] = 0

    # Step 2: 松弛所有边 V-1 次
    for _ in range(V):
        for u, v, weight in E:
            if distance[u] != float('inf') and distance[u] + weight < distance[v]:
                distance[v] = distance[u] + weight
                predecessor[v] = u

    # Step 3: 检测负权重环
    for u, v, weight in E:
        if distance[u] != float('inf') and distance[u] + weight < distance[v]:
            print("Graph contains negative weight cycle")
            return None, None

    return distance, predecessor

def find_path(src, target, predecessor):
    # 回溯路径
    path = []
    current = target
    while current != src:
        if current == -1:  # 如果当前节点为-1，说明路径不存在
            return []
        path.append(current)
        current = predecessor[current]
    path.append(src)
    path.reverse()  # 因为是从目标顶点回溯到源点，所以最后需要反转列表
    return path

# 示例用法
V = 7  # 顶点数（根据您的边列表调整）
E = [(1, 2, 6), (1, 3, 5), (1, 4, 5), (2, 5, -1), (3, 2, -2), (3, 5, 1), (4, 3, -2), (4, 6, -1), (5, 7, 3), (6, 7, 3)]  # 边的列表，(u, v, weight)

distance, predecessor = bellman_ford(V, E, 1)
if distance is not None:
    print("Distance from source:", distance[1:])  # 从 1 开始打印
    print("Predecessor in path:", predecessor[1:])

    # 获取从源点到顶点 7 的路径
    path = find_path(1, 7, predecessor)
    print("Path to vertex 7:", path)

