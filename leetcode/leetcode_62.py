def uniquePaths(m, n):
    """
    :type m: int
    :type n: int
    :rtype: int
    """
    row = [1] * n

    for i in range(m - 1):
        new_row = [1] * n
        for j in range(n - 2 , -1, -1):
            new_row[j] = new_row[j + 1] + row[j]
        row = new_row

    return row[0]

