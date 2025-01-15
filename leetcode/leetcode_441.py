def arrangeCoins(n):
    """
    :type n: int
    :rtype: int
    """
    # dp = [0] * (n)
    # dp[0] = 0
    # for i in range(1, n):
    #     dp[i] = dp[i - 1] + i
    #     if dp[i] > n:
    #         return i - 1
    #     if dp[i] == n :
    #         return i

    increment = 1
    num_stairs = 0
    coin_used = 0
    while coin_used <= n:
        coin_used += increment
        if coin_used > n:
            return num_stairs
        else:
            num_stairs += 1
            increment += 1







print(arrangeCoins(15))

