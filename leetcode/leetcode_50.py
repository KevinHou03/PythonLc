def myPow(x, n):
    is_neg = False
    if n < 0:
        is_neg = True
    a = x
    n = abs(n)
    for i in range(0, n - 1):
        x = x*a
    return x if is_neg is False else 1/x

print(myPow(2,-2))