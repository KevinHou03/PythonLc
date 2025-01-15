def minimumTotal(triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        memo = {} # 初始化备忘录来记录最短路径
        def aux(row, col):
            if row == len(triangle) - 1:
                return triangle[row][col]

            if (row, col) in memo:
                return memo[(row,col)]

            left = aux(row + 1, col)
            right = aux(row + 1, col + 1)

            memo[(row,col)] = triangle[row][col] + min(left, right)
            return memo[(row, col)]

        return aux(0,0)
'''
在递归算法中，有时会遇到重复计算的情况，比如同一个递归分支下，可能多次计算到相同的位置。记忆化就是一种缓存计算结果的技术：在每次计算时，如果之前已经计算过该位置的结果，就直接返回缓存的值，而不再重复计算。
'''


def minimumTotal2(triangle):
    """
    :type triangle: List[List[int]]
    :rtype: int
    """
    dp = [0] * (len(triangle) + 1)
    for row in triangle[::-1]:
        for i, val in enumerate(row):
            dp[i] = val + min(dp[i], dp[i + 1])

    return dp[0]

triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
print(minimumTotal2((triangle)))