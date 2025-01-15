import heapq


def nthUglyNumber(self, n):
    """
    :type n: int
    :rtype: int
    """
    # 使用minheap去操作，每找到一个ugly number，放进heap中，同时pop出来时把他的子ugly number放进去，并在剩余的ugly number中找最小值

    minheap = [1]
    visit = set()
    factor = [2,3,5]

    for i in range(n):
        num = heapq.heappop(minheap)
        if i == n - 1:
            return num
        for f in factor:
            if num * f not in visit: # 因为每个pop出来的数字 * factors可能会有重复！
                visit.add(num * f)
                heapq.heappush(minheap, num * f)


