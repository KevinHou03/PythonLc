def coinChange(coins, amount):
    """
    :type coins: List[int]
    :type amount: int
    :rtype: int
    """

    def recur(n):
        if n == 0:
            return 0
        result = float("inf")
        for coin in coins:
            if coin <= n:
                result = min(result, recur(n - coin) + 1)
        return result

    result = recur(amount)
    return result if result != float("inf") else -1


def coinChange2(coins, amount):
    """
    :type coins: List[int]
    :type amount: int
    :rtype: int
    """
    result = [float("inf")] * (amount + 1)
    result[0] = 0
    coin_used = [[] for _ in range(amount + 1)]

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                if result[i - coin] + 1 < result[i]:
                    result[i] = result[i - coin] + 1
                    coin_used[i] = coin_used[i - coin].copy()
                    coin_used[i].append(coin)

    print(coin_used[-1])
    print(result)

    return result[amount] if result[amount] != float("inf") else -1


print(coinChange2([1, 5, 6, 8], 11))


def coinChange3(coins, amount):
    """
    :type coins: List[int]
    :type amount: int
    :rtype: int
    """
    # 初始化最少硬币数量数组，所有值设为无穷大，除了第一个设为0
    result = [float("inf")] * (amount + 1)
    result[0] = 0

    # 初始化用于追踪每个金额所使用的硬币组合的数组
    coin_used = [[] for _ in range(amount + 1)]

    # 遍历每个金额，从1到amount
    for i in range(1, amount + 1):
        for coin in coins:  # 对于每个硬币
            if coin <= i:  # 如果当前硬币可以被使用（即不超过当前金额）
                # 如果通过当前硬币可以得到更少的硬币数量
                if result[i - coin] + 1 < result[i]:
                    result[i] = result[i - coin] + 1  # 更新最少硬币数量
                    coin_used[i] = coin_used[i - coin].copy()  # 复制前一个状态的硬币组合
                    coin_used[i].append(coin)  # 加入当前使用的硬币

    # 打印每个金额所使用的硬币组合
    for i, coins in enumerate(coin_used):
        print(f"Amount {i}: Coins used -> {coins}")

    # 返回结果：如果result[amount]不是无穷大，则返回该值；否则说明无法组成该金额，返回-1
    return result[amount] if result[amount] != float("inf") else -1


# 示例

print(coinChange3([1, 5, 6, 9], 10))



def coinChange(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for coin in coins:
        for x in range(coin, amount + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)

    return dp[amount] if dp[amount] != float('inf') else -1

def change(amount, coins):
    dp = [0] * (amount + 1)
    dp[0] = 1

    for coin in coins:
        for x in range(coin, amount + 1):
            dp[x] += dp[x - coin]

    return dp[amount]




def coinChange_2d_grid(coins, amount):
    """
    :type coins: List[int]
    :type amount: int
    :rtype: int
    """
    # 初始化DP表。所有值设为amount+1，表示无法凑成金额的默认值
    dp = [[amount + 1] * (amount + 1) for _ in range(len(coins) + 1)]

    # 设置当金额为0时所需的最小硬币数为0
    for i in range(len(coins) + 1):
        dp[i][0] = 0

    # 填充DP表
    for i in range(1, len(coins) + 1):
        for j in range(1, amount + 1):
            # 如果当前硬币面额大于当前金额j，不包括当前硬币种类
            if coins[i - 1] > j:
                dp[i][j] = dp[i - 1][j]
            else:
                # 包括当前硬币种类，并从两种情况中选择最小值
                # 1. 不使用当前硬币种类
                # 2. 使用当前硬币种类（减去当前硬币面额，然后加上这个硬币）
                dp[i][j] = min(dp[i - 1][j], dp[i][j - coins[i - 1]] + 1)

    print(dp)

    # 如果最终结果为amount + 1，则表示无法凑成金额
    return dp[len(coins)][amount] if dp[len(coins)][amount] != amount + 1 else -1


coinChange_2d_grid([1,3,4], 6)

