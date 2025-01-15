def search(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return True
        # 左右两边只有一边是有序的 当左边是有序的时候，left < mid
        while left <= right and nums[left] == nums[mid]:
            left += 1
        while left <= right and nums[right] == nums[mid]:
            right -= 1
        if nums[left] <= nums[mid]:
            # 如果目标在左侧，对左侧执行二分法
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return False


nums = [1,0,1,1,1]

print(search(nums,0))

def search2(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    left = 0
    right = len(nums) - 1

    while left <= right:
        left_ordered = True
        right_ordered = True
        mid = (left + right) // 2
        if nums[mid] == target:
            return True
        # 左右两边只有一边是有序的 当左边是有序的时候，left < mid
        if left == mid == 0:
            if nums[right] == target:
                return True
            else:
                return False
        for i in range(left, mid):
            if nums[i] > nums[i + 1]:
                left_ordered = False
                continue
        for i in range(mid, right):
            if nums[i] > nums[i + 1]:
                right_ordered = False
                continue
        if left_ordered and not right_ordered:
            # 如果目标在左侧，对左侧执行二分法
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return False



nums2 = [1,1,1,2,1,1]

print(search2(nums2,2))