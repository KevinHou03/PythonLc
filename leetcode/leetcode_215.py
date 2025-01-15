import heapq


def findKthLargest(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    nums = [-num for num in nums]
    heapq.heapify(nums)
    num = 0
    for i in range(k):
        num = heapq.heappop(nums)
    return -1*num

print(findKthLargest([3,2,3,1,2,4,5,5,6],4))


"""
quick select algorithm 
"""

def quickSelect(nums, k):
    k = len(nums) - k
    def quick_select(l, r):
        p = 0
        pivot = nums[r]
        for i in range(l,r):
            if nums[i] <= pivot:
                nums[p], nums[i] = nums[i], nums[p]
                p += 1
        nums[p], nums[r] = nums[r], nums[p]

        if k < p:
            quick_select(l, p - 1)
        elif k > p:
            quick_select(p + 1, r)
        else:
            return nums[p]

    return quick_select(0, len(nums) - 1)
