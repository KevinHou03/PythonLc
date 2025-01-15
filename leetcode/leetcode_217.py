def containsDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    di = {}
    for item in nums:
        if item not in di:
            di[item] = 1
        else:
            di[item] += 1
            return True

    return False

