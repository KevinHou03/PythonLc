def backtrack(s, left, right, n, result):
    if len(s) == 2 * n:
        if left == right == n:
            result.append(s)
        return

    if left < n:
        backtrack(s + '(', left + 1, right, n, result)

    if right < left:
        backtrack(s + ')', left, right + 1, n, result)


def generateParenthesis(n):
    result = []
    backtrack('', 0, 0, n, result)
    return result


print(generateParenthesis(3))