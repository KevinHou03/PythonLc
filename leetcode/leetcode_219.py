def containsNearbyDuplicate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: bool
    """
    cache = {}
    for i, val in enumerate(nums):
        if val in cache:
            if i - cache[val] <= k:
                print(cache)
                return True
        cache[val] = i
    print(cache)
    return False

print(containsNearbyDuplicate([1,2,3,1,2,3], 2))

