def matrixChainOrder(p):
    n = len(p) - 1  # 矩阵数量
    # m[i][j]为矩阵链Ai...Aj的最小乘法次数
    m = [[0 for x in range(n)] for x in range(n)]
    # s[i][j]记录了m[i][j]的最优解中的分割点
    s = [[0 for x in range(n)] for x in range(n)]
    # L是链的长度。
    for L in range(2, n + 1):
        for i in range(1, n - L + 2):
            j = i + L - 1
            m[i - 1][j - 1] = float('inf')
            for k in range(i, j):
                q = m[i - 1][k - 1] + m[k][j - 1] + p[i - 1] * p[k] * p[j]
                if q < m[i - 1][j - 1]:
                    m[i - 1][j - 1] = q
                    s[i - 1][j - 1] = k

    return m, s

def printOptimalParens(s, i, j):
    if i == j:
        print(f"A{i}", end='')
    else:
        print("(", end='')
        printOptimalParens(s, i, s[i - 1][j - 1])
        printOptimalParens(s, s[i - 1][j - 1] + 1, j)
        print(")", end='')

p = [5,10,3,12,5,50,6]# 矩阵维度数组
m, s = matrixChainOrder(p)
print("最少的乘法次数为：", m[0][len(p) - 2])# 输出最少乘法次数
print("最优乘法顺序为：")
printOptimalParens(s, 1, len(p) - 1)