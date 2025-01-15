def knows(a, b):
    pass


def findCelebrity(n):
    """
    :type n: int
    :rtype: int
    """
    candidate = 0
    for i in range(1, n):
        if knows(candidate, i):
            candidate = i

    for i in range(n):
        if i != candidate and (knows(candidate, i) or not knows(i, candidate)):
            return -1

    return candidate