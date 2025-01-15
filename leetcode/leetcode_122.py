def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    profit = 0
    left = 0
    right = 1
    while right < len(prices):
        if prices[right] > prices[left]:
            profit += (prices[right] - prices[left])
            left += 1
            right += 1
        else:
            left = right
            right +=1
    return profit

prices = [7,6,4,3,1]
print(maxProfit(prices))