


def maximalSquare(matrix):
    """
    :type matrix: List[List[str]]
    :rtype: int
    """
    rows = len(matrix)
    cols = len(matrix[0])

    memo = {} #记录已经标记过的左上角起始点

    def helper(row, col):
        if row >= rows or col >= cols:
            return 0

        if (row, col) not in memo:
            down = helper(row + 1, col)
            right = helper(row, col + 1)
            diag = helper(row + 1, col + 1)

           # memo[(row, col)] = 0
            if matrix[row][col] == '1':
                memo[(row, col)] = 1 + min(down, right, diag)
            else:
                memo[(row, col)] = 0

        return memo[(row, col)]

    helper(0, 0)
    return max(memo.values()) ** 2


def maximalSquare2(matrix):
    """
    :type matrix: List[List[str]]
    :rtype: int
    """
    rows = len(matrix)
    cols = len(matrix[0])
    dp = [[0] * (cols + 1) for j in range(rows + 1)]
    max_len = 0

    memo = {} #记录已经标记过的左上角起始点
    for row in range(rows - 1, -1, -1 ):
        for col in range(cols - 1, -1, -1):
            if matrix[row][col] == '1':
                dp[row][col] = 1 + min(dp[row + 1][col], dp[row][col + 1], dp[row + 1][col + 1])
                max_len = max(max_len, dp[row][col])
            else:
                dp[row][col] = 0
    return max_len **2


matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
print(maximalSquare2(matrix))

