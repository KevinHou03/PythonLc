from audioop import reverse


def makesquare(matchsticks):
    """
    :type matchsticks: List[int]
    :rtype: bool
    """
    if sum(matchsticks) % 4 != 0:
        return False
    side_length = sum(matchsticks) // 4
    sides = [0] * 4

    # 按长度降序排列火柴，贪心加速
    matchsticks.sort(reverse=True)

    # 用于记录状态的 memo
    memo = {}

    # 递归函数
    def backtrack(i):
        # 如果所有火柴都放置完毕，检查是否成功
        if i == len(matchsticks):
            return all(side == side_length for side in sides)

        # 当前状态（以元组表示）
        state = tuple(sorted(sides))
        if (i, state) in memo:
            return memo[(i, state)]

        # 尝试将当前火柴放到 4 条边之一
        for j in range(4):
            if sides[j] + matchsticks[i] <= side_length:
                sides[j] += matchsticks[i]
                if backtrack(i + 1):
                    memo[(i, state)] = True
                    return True
                sides[j] -= matchsticks[i]  # 回溯

        # 如果无法放置，记录状态为不可行
        memo[(i, state)] = False
        return False

    # 从第 0 根火柴开始
    return backtrack(0)
