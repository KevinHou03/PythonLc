def longestCommonSubsequence(X, Y):

    dict = {}
    x = len(X)
    y = len(Y)

    def backtrack(i, j):
        if i == 0 or j == 0:  # base case
            return 0, ""
        elif (i, j) in dict:
            return dict[i, j]
        else:
            if X[i - 1] == Y[j - 1]:
                len1, str1 = backtrack(i - 1, j - 1)
                dict[i, j] = (1 + len1, X[i - 1] + str1)

            else:
                left_len1, left_str1 = backtrack(i, j - 1)
                up_len1, up_str1 = backtrack(i - 1, j)
                if left_len1 > up_len1:
                    dict[i, j] = (left_len1,left_str1)
                else:
                    dict[i, j] = (up_len1, up_str1)
            return dict[i, j]

    len1, str1 = backtrack(x, y)
    return len1, str1


Y = "CGATAATTGAGA"
X = "GTTCCTAATA"

print(longestCommonSubsequence(X, Y))
