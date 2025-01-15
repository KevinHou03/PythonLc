import math


def numSquares(n):
    """
    :type n: int
    :rtype: int
    """
    # dp中每一个元素a代表组成数字a的perfect square的最小数量

    dp = [n] * (n + 1)
    dp[0] = 0
    squares = [x ** 2 for x in range(0, n) if x ** 2 <= n]
    for i in range(1, n + 1): # i 是每一次我们尝试的那个数字，也就是sub-problem
        for s in squares:
            square = s * s
            if i - square < 0:
                break
            dp[i] = min(dp[i], dp[i - square] + 1)

    return dp[n]

print(numSquares(10))