def consecutiveIncreasing(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    pivot = 0
    left = 0
    right = 1
    result = []
    while right <= len(nums) - 1:
        if nums[left] < nums[right]:
            right += 1
            left += 1

        else:
            result.append(right - pivot)
            pivot = right
            left = right
            right += 1


    result.append(right - pivot)

    print(result)

    return max(result)


def lengthOfLIS(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    dp = [1] * len(nums)


    for i in range(len(nums) - 1, -1, -1):
        for j in range(i + 1, len(nums)):
            if nums[j] >  nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)

print(lengthOfLIS([10,9,2,5,3,7,101,18]))
