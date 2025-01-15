def minDistance(A, B):
    m, n = len(A), len(B)
    # 创建一个二维数组 Edit，大小为 (m+1)x(n+1)
    Edit = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    # 初始化边界情况
    for j in range(n + 1):
        Edit[0][j] = j
    for i in range(1, m + 1):
        Edit[i][0] = i

    # 填充 Edit 数组
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            ins = Edit[i][j - 1] + 1
            del_ = Edit[i - 1][j] + 1
            if A[i - 1] == B[j - 1]:
                rep = Edit[i - 1][j - 1]
            else:
                rep = Edit[i - 1][j - 1] + 1

            Edit[i][j] = min(ins, del_, rep)

    TransposedEdit = [list(row) for row in zip(*Edit)]

    # 返回右下角的值，即为编辑距离
    return Edit[m][n],TransposedEdit


# 示例
A1 = "abcdef"
B1 = "akcdg"
result, Edit = minDistance(A1,B1)
print(minDistance(A1, B1))  # 应该输出编辑距离，对于这个例子是 3


def backtrackEditOperationsTransposed(Edit, A, B):
    i, j = len(A), len(B)
    operations = []

    while i > 0 or j > 0:
        if i > 0 and j > 0 and A[i-1] == B[j-1]:
            operations.append("No operation for '{}'".format(A[i-1]))
            i -= 1
            j -= 1
        elif i > 0 and j > 0 and Edit[j][i] == Edit[j-1][i-1] + 1:
            operations.append("Replace '{}' in A with '{}' from B".format(A[i-1], B[j-1]))
            i -= 1
            j -= 1
        elif i > 0 and Edit[j][i] == Edit[j][i-1] + 1:
            operations.append("Delete '{}' from A".format(A[i-1]))
            i -= 1
        elif j > 0 and Edit[j][i] == Edit[j-1][i] + 1:
            operations.append("Insert '{}' from B into A".format(B[j-1]))
            j -= 1
        else:
            # 处理边界情况
            if i > 0:
                i -= 1
                operations.append("Delete '{}' from A".format(A[i]))
            elif j > 0:
                j -= 1
                operations.append("Insert '{}' from B into A".format(B[j]))

    return operations[::-1]  # 反转列表以获得从头到尾的顺序



print(backtrackEditOperationsTransposed(Edit, A1, B1))

