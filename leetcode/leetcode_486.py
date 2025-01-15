# 定义 dp[i][j] 表示在数组 nums[i:j+1] 范围内，当前玩家能获得的最大净分（自己得分 - 对手得分）

def predictTheWinner(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    n = len(nums)
    dp = [[0] * n for _ in range(n)]

    for i in range(n):
        dp[i][i] = nums[i]

    for lens in range(2, n + 1): #区间长度
        for i in range(0, n - lens + 1):
            j = i + lens - 1
            dp[i][j] = max(nums[i] - dp[i + 1][j], nums[j] - dp[i][j - 1])


    return dp[0][n - 1]


