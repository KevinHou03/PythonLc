# THIS CODE IS MY OWN WORK, IT WAS WRITTEN WITHOUT CONSULTING
#
# A TUTOR OR CODE WRITTEN BY OTHER STUDENTS - Kaiyuan Hou

def minDistance(word1, word2):

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

    return grid[0][0], grid


def backtracing(grid, word1, word2):
    delete = 0
    insert = 0
    replace = 0

    i = 0
    j = 0

    while i < len(word1) or j < len(word2):

        if i >= len(word1):
            while j < len(word2):
                print("INSERT", word2[j])
                insert += 1
                j += 1
            break
        if j >= len(word2):
            while i < len(word1):
                print("DELETE", word1[i])
                delete += 1
                i += 1
            break
        if word1[i] == word2[j]:
            i += 1
            j += 1
        elif grid[i][j] == grid[i + 1][j] + 1:
            delete += 1
            print("DELETE", word1[i])
            i = i + 1
        elif grid[i][j] == grid[i][j + 1] + 1:
            insert += 1
            print("INSERT", word2[j])
            j = j + 1
        elif grid[i][j] == grid[i + 1][j + 1] + 1:
            print("Substitute", word1[i], "with", word2[j])
            replace += 1
            i = i + 1
            j = j + 1

    print("")
    print("Number of Insertions:", insert,"\n"
          "Number of Deletions", delete,"\n"
          "Number of Substitutions", replace, "\n"
          "Total number of operations", insert + delete + replace)

    return delete, insert, replace


word1 = input()
word2 = input()
total_steps, grid = minDistance(word1, word2)
print("Levenshtein distance:", total_steps)
print("")
print("The specific edit operations as per the Dynamic Programming table are as follows :")
print("")
print(backtracing(grid, word1, word2))

print(grid)

