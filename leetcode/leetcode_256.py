def minCost(costs):
    """
    :type costs: List[List[int]]
    :rtype: int
    """
    if not costs:
        return 0

    dp = [[0] * 3 for k in range(len(costs))]

    dp[0][0] = costs[0][0]
    dp[0][1] = costs[0][1]
    dp[0][2] = costs[0][2]

    for i in range(1, len(costs)):
        dp[i][0] = costs[i][0] + min(dp[i - 1][1], dp[i - 1][2])
        dp[i][1] = costs[i][1] + min(dp[i - 1][0], dp[i - 1][2])
        dp[i][2] = costs[i][2] + min(dp[i - 1][0], dp[i - 1][1])

    n = len(costs)
    return min(dp[n-1][0], dp[n-1][1], dp[n-1][2])
