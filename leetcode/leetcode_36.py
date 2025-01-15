def isValidSudoku(board):
    """
    :type board: List[List[str]]
    :rtype: bool
    """
    true_set = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
    for k in range(9):
        validation_row = []
        validation_col = []
        for j in range(9):
            if board[k][j] in true_set:
                validation_row.append(board[k][j])
            if board[j][k] in true_set:
                validation_col.append(board[j][k])
        if len(set(validation_row)) != len(validation_row) or len(set(validation_col)) != len(validation_col):
            return False
    # for k in range(9):
    #     validation_col = []
    #     for j in range(9):
    #         if board[j][k] in true_set:
    #             validation_col.append(board[j][k])
    #     if len(set(validation_col)) != len(validation_col):
    #         return False

    for k in range(0, 9, 3):
        for j in range(0, 9, 3):
            sub_board = []
            sub_board = [board[x][y] for x in range(k, k + 3) for y in range(j, j + 3)]
            sub_board_validated =[element for element in sub_board if element in true_set]
            if len(sub_board_validated) != len(set(sub_board_validated)):
                return False

    return True


board = [["5", "3", ".", ".", "7", ".", ".", ".", "."]
    , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
    , [".", "9", "8", ".", ".", ".", ".", "6", "."]
    , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
    , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
    , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
    , [".", "6", ".", ".", ".", ".", "2", "8", "."]
    , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
    , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

print(isValidSudoku(board))
for i in range(0, 9, 3):
    print(i)  # 0,3,6
