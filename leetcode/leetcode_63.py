def check_row_all_ones(matrix, index):
    return all(matrix[index])

def check_col_all_ones(matrix, index):
    return all(row[index] for row in matrix)

def uniquePathsWithObstacles(obstacleGrid):
    """
    :type obstacleGrid: List[List[int]]
    :rtype: int
    """
    if obstacleGrid[0][0] == 1:
        return 0

    m, n = len(obstacleGrid), len(obstacleGrid[0])
    row_blocked = False
    col_blocked = False

    if obstacleGrid[0][0] == 1:
        return 0

    if m == 1 or n == 1:
        if m == 1:
            for i in range(n):
                if obstacleGrid[0][i] == 1:
                    return 0
            return 1
        else:
            for i in range(m):
                if obstacleGrid[i][0] == 1:
                    return 0
            return 1

    for i in range(1, m):
        if obstacleGrid[i][0] == 1:
            obstacleGrid[i][0] = 0
        else:
            obstacleGrid[i][0] = 1
    for j in range(1, n):
        if obstacleGrid[0][j] == 1:
            obstacleGrid[0][j] = 0
        else:
            obstacleGrid[0][j] = 1

    for x in range(1, m):
        for y in range(1, n):
            if obstacleGrid[x][y] == 1:
                print("an obstacle detected")
                row_blocked = False
                col_blocked = False
                for z in range(x, m):
                    if obstacleGrid[z][y] == 0:

                        row_blocked = True
                        break
                for z in range(y, n):
                    if obstacleGrid[x][z] == 0:
                        col_blocked = True
                        break
                if row_blocked is True or col_blocked is True:
                    print("is 0")
                    return 0
                print(row_blocked, col_blocked)
                obstacleGrid[x][y] = 0
            else:
                obstacleGrid[x][y] = obstacleGrid[x][y - 1] + obstacleGrid[x - 1][y]
    return obstacleGrid[m - 1][n - 1]


obstacleGrid =[[0,0,0],[0,1,0],[0,0,0]]
print(uniquePathsWithObstacles(obstacleGrid))
