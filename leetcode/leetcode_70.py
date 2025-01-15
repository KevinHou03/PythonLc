def climbStairs(n):
    """
    :type n: int
    :rtype: int
    """
    if n == 0 or n == 1:
        return 1
    else:
        steps = [0] * (n + 1)
        steps[0] = 1
        steps[1] = 1
        for i in range(2, n + 1):
            steps[i] = steps[i - 2] + steps[i - 1]
    return steps[-1]

print(climbStairs(3))


def climb2(n):
    if n == 0 or n == 1:
        return 1

    return climb2(n - 1) + climb2(n - 2)


print(climb2(38))