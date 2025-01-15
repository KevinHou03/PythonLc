def floyd_warshall(n, edges):
    # 创建距离矩阵和前驱节点矩阵
    dist = [[float('inf')] * n for _ in range(n)]
    pred = [[None] * n for _ in range(n)]

    # 初始化距离矩阵和前驱节点矩阵
    for i in range(n):
        dist[i][i] = 0  # 每个顶点到自己的距离为0

    for u, v, weight in edges:
        dist[u][v] = weight
        pred[u][v] = u  # 初始化前驱节点为起点

    # Floyd-Warshall 算法主体
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    pred[i][j] = pred[k][j]  # 更新前驱节点
                print(dist)

    return dist, pred


def construct_path(u, v, pred):
    """ 通过前驱节点矩阵构建路径 """
    if pred[u][v] is None:
        return None  # 没有路径

    path = []
    while v is not None and v != u:
        path.append(v)
        v = pred[u][v]
    path.append(u)
    path.reverse()

    return path


# 示例用法
n = 4  # 顶点数量
edges = [(0, 1, 3), (0, 2, 7), (1, 2, 1), (1, 3, 5), (2, 3, 2)]  # 边的列表，格式为 (u, v, weight)

distances, predecessors = floyd_warshall(n, edges)
print("Distance matrix:")
for row in distances:
    print(row)

print("Predecessor matrix:")
for row in predecessors:
    print(row)

# 获取从顶点 0 到顶点 3 的路径
path = construct_path(0, 3, predecessors)
print("Path from 0 to 3:", path)
