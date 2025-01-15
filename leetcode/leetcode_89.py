def grayCode(n):
    """
    :type n: int
    :rtype: List[int]
    """

    ans = [0,1]
    for i in range(1, n):
        temp = ans
        ans.reverse()
        for item in ans:
            pass
