def summaryRanges(nums):
    """
    :type nums: List[int]
    :rtype: List[str]
    """

    mark = 0
    left = 0
    right = 1
    ans = []
    while right < len(nums):
        if nums[left] == nums[right] - 1:
            left += 1
            right += 1
        else:
            if nums[mark] == nums[left]:
                ans.append(nums[mark])
            else:
                ans.append([nums[mark], nums[left]])
            mark = right
            right += 1
            left += 1
    if nums[mark] == nums[right - 1]:
        ans.append([nums[mark]])
    else:
        ans.append([nums[mark], nums[right - 1]])
    return ans

print(summaryRanges([0,4,5,6,8,9,10,11,24,27,28]))
