def numberOfArithmeticSlices(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    count = 0
    result = 0
    for i in range(2, len(nums) - 1):
        if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
            count += 1
            result += count
        else:
            count = 0
    return result

