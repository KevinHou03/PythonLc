def setZeroes(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: None Do not return anything, modify matrix in-place instead.
    """
    #
    row_num = len(matrix)
    col_num = len(matrix[0])
    zero_row = set()
    zero_col = set()
    # result = [[9 for _ in range(col_num)] for _ in range(row_num)]
    for i in range(row_num):
        for j in range(col_num):
            if matrix[i][j] == 0:
                zero_row.add(i)
                zero_col.add(j)

    for i in range(row_num):
        for j in range(col_num):
            if i in zero_row or j in zero_col:
                matrix[i][j] = 0

    return matrix


m1 = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
m2 = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
print(setZeroes(m1))
