def combine(n, k):
    """
    :type n: int
    :type k: int
    :rtype: List[List[int]]
    """
    result = []

    def backtrack(start, cur_comb):
        # base case
        if len(cur_comb) == k:
            result.append(cur_comb[:])
            return

        for i in range(1, n + 1):
            cur_comb.append(i)
            backtrack(i + 1, cur_comb)
            cur_comb.pop()

    backtrack(1, [])
    return result


print(combine(4, 2))

'''
backtract(1) [1] -> backtrack(2) [1,2] -> [1,]
'''
