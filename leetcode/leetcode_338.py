def countBits(n):
    """
    :type n: int
    :rtype: List[int]
    """

    bits = []

    while n > 0:
        bits.append(n % 2)
        n = n // 2

countBits(9)

def countBits2(n):
    dp = [0] * (n + 1)
    dp[0] = 0


    for i in range(1, n + 1):
        dp[i] = dp[i // 2] + i % 2
    return dp

print(countBits2(5))
