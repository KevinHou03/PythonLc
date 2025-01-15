def minDistance(word1, word2):
    """
    :type word1: str
    :type word2: str
    :rtype: int
    """
    grid = [[float("inf") for _ in range(len(word2) + 1)] for _ in range(len(word1) + 1)]

    for j in range(len(word2) + 1):
        grid[len(word1)][j] = len(word2) - j
    for i in range(len(word1) + 1):
        grid[i][len(word2)] = len(word1) - i

    for i in range(len(word1) - 1, -1, -1):
        for j in range(len(word2) - 1, -1, -1):
            if word1[i] == word2[j]:
                grid[i][j] = grid[i + 1][j + 1]
            else:
                grid[i][j] = 1 + min(grid[i + 1][j], grid[i][j + 1], grid[i + 1][j + 1])

    return grid[0][0],grid


print(minDistance("abcdef","akcdg"))

