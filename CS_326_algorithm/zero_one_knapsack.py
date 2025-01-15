# THIS CODE IS MY OWN WORK, IT WAS WRITTEN WITHOUT CONSULTING
# A TUTOR OR CODE WRITTEN BY OTHER STUDENTS - Kevin Hou
def knapsack(limit, weight, profit):
    num_items = len(profit)
    grid = [[0 for i in range(limit + 1)] for j in range(num_items + 1)]

    for i in range(1, num_items + 1):
        for j in range(1, limit + 1):
            if weight[i - 1] <= j:
                grid[i][j] = max(grid[i - 1][j], grid[i - 1][j - weight[i - 1]] + profit[i - 1])
            else:
                grid[i][j] = grid[i - 1][j]  #

    i = num_items
    j = limit
    target = grid[i][j]
    result = []
    while target != 0 and i > 0:
        if target != grid[i - 1][j]:
            result.append(i - 1)
            target -= profit[i - 1]
            while j >= 0 and grid[i - 1][j] != target:
                j -= 1
        else:
            i -= 1
        if j < 0:
            break
    return grid, result, grid[-1][-1]

grid, result, total_profit = knapsack(25, [24, 10, 10, 7], [12, 8, 9, 5])
print(grid)
print(result)
print(total_profit)





