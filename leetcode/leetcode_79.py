def has_neighbor(matrix, row, col, target):  # 判断m[i][j]的邻居里有没有target
    res = []
    if matrix[row + 1][col] == target:
        res.append([row + 1, col])
    if matrix[row - 1][col] == target:
        res.append([row - 1, col])
    if matrix[row][col + 1] == target:
        res.append([row, col + 1])
    if matrix[row][col - 1] == target:
        res.append([row, col - 1])
    else:
        return -1
    return res


def exist(board, word):
    """
    :type board: List[List[str]]
    :type word: str
    :rtype: bool
    """
    rows, cols = len(board), len(board[0])
    path = set()

    def backtrack(cur_row, cur_col, i):  # i is the ith letter of the target word.
        if i == len(word):
            return True

        if cur_row < 0 or cur_col < 0 or cur_row >= rows or cur_col >= cols or word[i] != board[cur_row][cur_col] or (
                cur_row, cur_col) in path:
            return False

        path.add((cur_row, cur_col))
        res = (backtrack(cur_row + 1, cur_col, i + 1) or
               backtrack(cur_row, cur_col + 1, i + 1) or
               backtrack(cur_row - 1, cur_col, i + 1) or
               backtrack(cur_row, cur_col - 1, i + 1))

        path.remove((cur_row, cur_col))
        return res

    for i in range(rows):
        for j in range(cols):
            if backtrack(i, j, 0): return True
    return False
