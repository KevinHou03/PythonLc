def maximumGap(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    ans = 0
    nums.sort()
    for i in range(len(nums) - 1):
        next = i + 1
        ans = max(abs(ans), abs(nums[next] - nums[i]))
    return ans

nums = [3,6,9,4,19,2]
print(maximumGap(nums))