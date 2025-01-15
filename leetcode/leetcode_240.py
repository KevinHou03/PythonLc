def searchMatrix(matrix, target):
    """
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
    """
    #关键在于 从left bottom开始搜索，如果小于target，则这一列不用考虑了，如果大于target，这一行不用考虑了
    r = len(matrix) - 1
    c = 0

    while r >= 0 and c < len(matrix[0]):
        if matrix[r][c] == target:
            return True
        elif matrix[r][c] < target:
            c += 1
        else:
            r -= 1
    return False

matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
print(searchMatrix(matrix,5))