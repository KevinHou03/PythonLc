def searchMatrix(matrix, target):
    """
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
    """
    left = 0
    right = len(matrix) - 1
    i = 0
    while left <= right:
        mid = (left + right) // 2
        if matrix[mid][0] <= target <= matrix[mid][len(matrix[0]) - 1]:
            i = mid
            left = matrix[i][0]
            right = matrix[i][len(matrix[0]) - 1]
            if left <= target <= right:
                new_left = 0  # matrix[i][0]
                new_right = len(matrix[0]) - 1  # matrix[i][len(matrix[0]) - 1]
                while new_left <= new_right:
                    mid = (new_left + new_right) // 2
                    if matrix[i][mid] == target:
                        return True
                    elif matrix[i][mid] < target:
                        new_left = mid + 1
                    else:
                        new_right = mid - 1
            break
        elif matrix[mid][0] > target:
            right = mid - 1
        elif matrix[mid][len(matrix[0]) - 1] < target:
            left = mid + 1
    return False





array = [1,2,3]

array.sort()


m1 = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
print(searchMatrix(m1, 12))
