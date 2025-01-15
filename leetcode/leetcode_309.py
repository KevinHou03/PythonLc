def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    """
     if buy: i + 1
     if sell: i + 2 automatically skipping one day for the cooldown 
    """
    dp = {} # key:(index in the prices, buy or sell?).  value: max_profit

    def dfs(i, buy):
        if i >= len(prices):
            return 0
        if (i, buy) in dp:
            return dp[(i, buy)] # 返回的是profit
        if buy: #如果是买
            buying = dfs(i + 1, not  buy) - prices[i] #如果你这次是买，那下次就只能是卖了
            cooldown = dfs(i + 1, buy) #如果这次是cooldown，（把它和buy放在一起了）那什么都不用变
            dp[(i, buy)] = max(buying, cooldown )
        else:# if sell
            selling = dfs(i + 2, not buy) + prices[i]
            cooldown = dfs(i + 1, buy)
            dp[(i, buy)] = max(selling, cooldown)

        return dp[(i, buy)]

    return dfs(0, True)

