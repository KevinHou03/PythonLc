def spiralOrder(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[int]
    """
    top = 0
    buttom = len(matrix) - 1
    left = 0
    right = len(matrix[0]) - 1
    result = []

    if len(matrix) == 1 and len(matrix[0]) == 1:
        result.append(matrix[0][0])
        return result

    while left <= right and top <= buttom:
        for i in range(left, right + 1):
            result.append(matrix[top][i])
        top += 1

        for i in range(top, buttom + 1):
            result.append(matrix[i][right])
        right -= 1

        if top <= buttom:
            print("ds")
            for i in range(right, left - 1, -1):
                result.append(matrix[buttom][i])
            buttom -= 1

        if left <= right:
            print("shd")
            for i in range(buttom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1
        # if len(matrix) == len(matrix[0]) and len(matrix) % 2 == 1:
        #     result.append(matrix[len(matrix) // 2][len(matrix) // 2])


    return result


matrix = [[1]]
print(spiralOrder(matrix))
