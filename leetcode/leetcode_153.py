def findMin(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    left = 0
    right = len(nums) - 1
    ans = nums[0]
    while left <= right:
        if nums[left] < nums[right]:
            ans = min(ans, nums[left])
            break

        mid = (left + right) // 2
        ans = min(nums[mid], ans)
        if nums[mid] < nums[left]: # search left
            right = mid - 1
        else: # search right
            left = mid + 1

    return ans


nums = [3,4,5,1,2]
print(findMin(nums))