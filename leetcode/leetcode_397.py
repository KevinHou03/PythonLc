def integerReplacement(n):
    """
    :type n: int
    :rtype: int
    """
    def backtrack(new_n):
        if new_n == 1:
            return 0
        if new_n % 2 == 0:
            return 1 + backtrack(new_n / 2)
        else:
            return 1 + min(backtrack(new_n + 1), backtrack(new_n - 1))

    return backtrack(n)


print(integerReplacement(1))


def integerReplacement2(n):
    memo = {}


    def dfs(num):
        if num == 1:
            return 0
        if num in memo:
            return memo[num]

        if num % 2 == 0:
            memo[num] = 1 + dfs(num // 2)
        else:
            memo[num] = 1 + min(dfs(num + 1), dfs(num - 1))

        return memo[num]


    return dfs(n)