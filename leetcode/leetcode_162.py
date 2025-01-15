def findPeakElement(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    l = 0
    r = len(nums) - 1

    while l <= r:
        m = l + ((r - l) // 2)
        if m + 1 < len(nums) and m - 1 >= 0 and nums[m] > nums[m+1] and nums[m] > nums[m-1]:
            return m
        if m > 0 and  nums[m] < nums[m - 1]:
            r = m - 1
        elif m < len(nums) - 1 and nums[m] < nums[m + 1]:
            l = m + 1
        else:
            return m



nums = [1]
print(findPeakElement(nums))

