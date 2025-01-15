def rotate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    nums_copy = nums[:]
    for i, val in enumerate(nums):
        nums[(i + k) % len(nums)] = nums_copy[i]
    return nums


nums = [1,2,3,4,5,6,7]
print(rotate(nums, 2))

def rotateO1(nums, k):
    left, right = 0, len(nums) - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1

    left, right = 0, k - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1

    left = k
    right = len(nums) - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1

nums = [1,2,3,4,5,6,7]
print(rotateO1(nums, 2))