def countPrimes(n):
    """
    :type n: int
    :rtype: int
    """
    if n < 2:
        return 0

    is_prime = [True] * n
    is_prime[0] = False
    is_prime[1] = False

    counter = 0

    for i in range(2, n - 1):
        if is_prime[i]:
            for j in range(i*2,n,i):
                is_prime[j] = False
            print(is_prime)

    for item in is_prime:
        if item:
            counter += 1

    return counter

print(countPrimes(100))
