def missingNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    d = set(nums)
    for i in range(min(nums), max(nums) + 1):
        if i not in d:
            return i
    return max(nums) + 1

print(missingNumber([1,2,3,4,5,7,8,9]))

