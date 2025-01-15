def countNumbersWithUniqueDigits(n):
    """
    :type n: int
    :rtype: int
    """
    count = 10 # i = 1的情况
    unique_digits = 9 # 当有10i个digit的时候有多少个数字是符合要求的unique digit number？
    available_number = 9

    for i in range(2, n + 1):
        unique_digits *= available_number
        count = count + unique_digits
        available_number -= 1


    return count


print(countNumbersWithUniqueDigits(3))
