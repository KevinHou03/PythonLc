# good solution link: https://www.youtube.com/watch?v=fMSJSS7eO1w

def rotate(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: None Do not return anything, modify matrix in-place instead.
    """
    left = 0
    right = len(matrix[0] - 1)

    while left < right:
        for i in range(right - left):  # 这里尝试一下 range(len(matrix[0]) - 2)
            top = left
            buttom = right

            # save top left value, then reversely substitute
            topleft = matrix[top][left + i]  # this is a dynamic value, cannot be matrix[0][0]要不然你下一个inner怎么办
            # move buttom left into top left
            matrix[top][left + i] = matrix[buttom - i][left]
            matrix[buttom - i][left] = matrix[buttom][right - i]
            matrix[buttom][right - i] = matrix[top + i][right]
            matrix[top + i][right] = topleft
            #
            # temp = matrix[top ][left + 1]
            # matrix[top][left + 1] = matrix[buttom - 1][left]
            # matrix[buttom - 1][left] = matrix[buttom][right - 1]
            # matrix[buttom][right - 1] = matrix[top + 1][right]
            # matrix[top + 1][right] = temp

            left += 1
            right -= 1
            


