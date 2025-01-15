# memoization recursive solution:双指针
def isInterleave(self, s1, s2, s3):
    """
    :type s1: str
    :type s2: str
    :type s3: str
    :rtype: bool
    """
    if len(s1) + len(s2) != len(s3):
        return False
    memo = {}

    def dfs(i, j):  # dfs是因为在两个substr都有同一个的时候，要像decision tree一样分支，分成两种情况看
        if i == len(s1) and j == len(s2):  # 两个都到头了
            return True
        if (i, j) in memo:
            return memo[(i, j)]
        if i < len(s1) and s1[i] == s3[i + j] and dfs(i + 1, j):
            memo[(i, j)] = True
            return True
        if j < len(s2) and s2[j] == s3[i + j] and dfs(i, j + 1):
            memo[(i, j)] = True
            return True
        memo[(i, j)] = False
        return False

    return dfs(0, 0)

def isInterleave_DP(self, s1, s2, s3):
    """
    :type s1: str
    :type s2: str
    :type s3: str
    :rtype: bool
    """

    if len(s1) + len(s2) != len(s3):
        return False

    dp = [[False] * (len(s2) + 1) for i in range(len(s1) + 1)]
    dp[len(s1)][len(s2)] = True

    for i in range(len(s1), -1, -1): # 5 4 3 2 1 0
        for j in range(len(s2), -1, -1):
            if i < len(s1) and s1[i] == s3[i + j] and dp[i + 1][j]:
                dp[i][j] = True
            if j < len(s2) and s2[j] == s3[i + j] and dp[i][j + 1]:
                dp[i][j] = True
    return dp[0][0]


