def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    dp = [[0] * 5 for _ in range(len(prices))]
    dp[0][0] = 0  # 第 0 天不进行交易
    dp[0][1] = -prices[0]  # 第 0 天第一次买入
    dp[0][2] = 0  # 第 0 天第一次卖出（还未发生）
    dp[0][3] = -prices[0]  # 第 0 天第二次买入（还未发生）
    dp[0][4] = 0
    for i in range(1, len(prices)):
        dp[i][0] = dp[i-1][0] #不持有
        dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i]) #第一次买入
        dp[i][2] = max(dp[i-1][2], dp[i-1][1] + prices[i])# 第一次卖出
        dp[i][3] = max(dp[i-1][3], dp[i-1][2] - prices[i]) #第二次买入
        dp[i][4] = max(dp[i-1][4], dp[i-1][3] + prices[i]) #第二次卖出

    return max(dp[len(prices)-1][2], dp[len(prices)-1][4])


prices = [3,3,5,0,0,3,1,4]
print(maxProfit(prices))


def maxProfit2(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    dp0 = 0  # 第 0 天不进行交易
    dp1 = -prices[0]  # 第 0 天第一次买入
    dp2 = 0  # 第 0 天第一次卖出（还未发生）
    dp3 = -prices[0]  # 第 0 天第二次买入（还未发生）
    dp4 = 0
    for i in range(1, len(prices)):
        dp0 = dp0 #不持有
        dp1 = max(0, dp0 - prices[i]) #第一次买入
        dp2 = max(dp2, dp1 + prices[i])# 第一次卖出
        dp3 = max(dp3, dp2 - prices[i]) #第二次买入
        dp4 = max(dp4, dp3 + prices[i]) #第二次卖出

    return max(dp2, dp4)

print(maxProfit(prices))