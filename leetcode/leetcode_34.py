def searchRange(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    flag = False
    if target not in nums:
        return [-1, -1]
    result = []
    target_index = nums.index(target)
    result.append(target_index)
    # if target_index + 1 == len(nums):
    #     return [target_index,target_index]
    while nums[target_index] == target:
        if target_index == len(nums) - 1:
            flag = True
            break
        target_index += 1
    if flag:
        result.append(target_index)
    else:
        result.append(target_index - 1)

    return result


nums = [2, 2, 2, 3, 3]
print(searchRange(nums, 3))


def searchRange2(nums, target):
    if target not in nums:
        return [-1, -1]

    left, right = 0, len(nums) - 1
    for i in range(0, len(nums)):
        if nums[i] == target:
            left = i
            break
    for j in range(len(nums) - 1, -1, -1):
        if nums[j] == target:
            right = j
            break

    return [left, right]


nums2 = [1, 2, 2, 3, 3, 3, 4, 5, 6]
print(searchRange2(nums2, 3))


def searchRange3(nums, target):
    if target not in nums:
        return [-1, -1]
    left, right = -1, -1
    for i in range(0, len(nums) - 1):
        if nums[i] == target:
            if left == -1:
                left = i
            right = i

    return [left, right]


def searchRange4(nums, target):  # 二分法
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
    print(left)
        # else:
        #     right = mid - 1



nums3 = [1, 2, 2, 3, 3, 3, 4, 5, 6]
searchRange2(nums3, 3)