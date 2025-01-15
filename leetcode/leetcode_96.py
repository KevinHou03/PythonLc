def numTrees(n):
    """
    :type n: int
    :rtype: int
    """

    def count(left, right):
        memoization = {}
        if left >= right:
            return 1
        if (left, right) in memoization:
            return memoization[(left,right)]
        res = 0
        for node in range(left, right + 1):
            right_tree = count(node + 1, right)
            left_tree =  count(left, node  - 1)
            res += left_tree * right_tree
        memoization[(left, right)]  = res
        return res

    return count(1, n)

print(numTrees(9))

def numTrees2(n):
    """
    :type n: int
    :rtype: int
    """
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1

    for i in range(2, n + 1):
        for root in range(1, i + 1):
            dp[i] += dp[root - 1] * dp[i - root]
    return dp[n]

print(numTrees2(9))