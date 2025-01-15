def find_all_combination(n): #To find all positive integer combinations such that their sum equals a given number using backtracking
    result = []
    def backtrack(start, cur_target, path):
        if cur_target == 0:
            result.append(path[:])
            return

        for i in range(start, cur_target + 1):
            path.append(i)
            backtrack(i, cur_target - i, path)
            path.pop()

    backtrack(1, n, [])
    return result


print(find_all_combination(5))



def integerBreak(n):
    """
    :type n: int
    :rtype: int
    """
    pass

def find_all_combination_wproduct(n):  # To find all positive integer combinations such that their sum equals a given number using backtracking
    result = []
    max_p = [0]

    def backtrack(start, cur_target, path,cur_product):
        if cur_target == 0:
            result.append(path[:])
            if len(path) >= 2:
                max_p[0] = max(max_p[0], cur_product )
            return

        for i in range(start, cur_target + 1):
            path.append(i)
            backtrack(i, cur_target - i, path, cur_product * i)
            path.pop()

    backtrack(1, n, [], 1)
    return result, max_p[0]

print(find_all_combination_wproduct(2))


def dp(n):
    """
    :type n: int
    :param n:
    :return:
    不断的把一个数字分成两个部分，only 两个，dp[i]表示把i分成两个部分j和i-j, 那么最大值
    可能是dp[i],j*(i - j), j*dp[i - j]
    """
    dp = [0] * (n + 1)
    dp[1] = 0

    for i in range(2, n + 1):
        for j in range(1, i):
            dp[i] = max(dp[i],j * (i - j), j + dp[i - j])
    return dp[n]

print(dp(5))


