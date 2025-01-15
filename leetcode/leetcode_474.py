def findMaxForm(strs, m, n):
    """
    :type strs: List[str]
    :type m: int
    :type n: int
    :rtype: int
    """
    # memoization

    memo = {}

    def dfs(i, m, n):
        if i == len(strs):
            return 0
        if (i, m, n) in memo:
            return memo[(i, m, n)]
        m_count, n_count = strs[i].count("0"), strs[i].count("1")
        memo[(i, m, n)] = dfs(i + 1, m, n)
        if m_count < m and n_count < n:
            memo[(i, m, n)] = max(dfs(i + 1, m, n), 1 + dfs(i + 1, m - m_count, n - n_count))
        return memo[(i, m, n)]

    return dfs(0,0,0)


