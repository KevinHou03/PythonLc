def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    max_profit = 0
    for i, val in enumerate(prices):
        for j, val2 in enumerate(prices[i + 1:]):
            if val2 > val:
                max_profit = max(max_profit, val2 - val)
    return max_profit


def maxProfit2(prices):
    left = 0
    right = 1
    max_profit = 0
    while right < len(prices):
        if prices[left] < prices[right]:
            max_profit = max(max_profit, prices[right] - prices[left])
            right += 1
        else:
            left = right
            right = left + 1
    return max_profit


prices = [7,1,5,3,6,4]
def maxProfit3(prices):
    profit = 0
    for i in range(len(prices)):
        max_profit = maxProfit2(prices[i:])
    return profit

print(maxProfit3(prices))





