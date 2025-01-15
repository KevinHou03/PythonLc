def fibonacci(n):

    result = [0] * (n + 1)
    result[0] = 0
    result[1] = 1
    for i in range(2, n + 1):
        result[i] = result[i - 2] + result[i - 1]
    return result

print(fibonacci(9))
