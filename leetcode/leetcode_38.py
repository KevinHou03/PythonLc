def countAndSay(n):
    """
    :type n: int
    :rtype: str
    """
    if n == 1:
        return "1"
    prev = countAndSay(n - 1)
    result = ""
    count = 1

    for i in range(len(prev) - 1):
        if prev[i] == prev[i + 1]:
            count += 1
        else:
            result += str(count) + prev[i]
            count = 1
    result += str(count) + prev[-1]

    return result


print(countAndSay(5))
