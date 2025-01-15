import heapq


def nthSuperUglyNumber(n, primes):
    """
    :type n: int
    :type primes: List[int]
    :rtype: int
    """

    minheap = [1]
    visited = set(minheap)
    factors = primes

    for i in range(n):
        num = heapq.heappop(minheap)
        if i == n - 1:
            return num
        for f in factors:
            new_num = f * num
            if new_num not in visited:
                heapq.heappush(minheap, new_num)
                visited.add(new_num)


n = 1
primes = [2,3,5]

print(nthSuperUglyNumber(n, primes))