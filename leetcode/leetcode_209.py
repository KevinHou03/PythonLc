def minSubArrayLen(target, nums):
    """
    :type target: int
    :type nums: List[int]
    :rtype: int
    """
    l = 0
    cur_sum = 0
    min_len = float('inf')

    for r in range(len(nums)):
        cur_sum += nums[r]

        while cur_sum > target:
            cur_sum -= nums[l]
            min_len = min(min_len, r - l + 1)
            l += 1

    if min_len == float('inf'):
        return 0
    else:
        return min_len

print(minSubArrayLen(11, [1,1,1,1,1,1,1,1]))


def minSubArrayLen2(target, nums):
    nums = [1]
    f2, f3, f5 = 0, 0, 0

    for r in range(1,n):
        num = min(nums[f2]*2, nums[f3]*3, nums[f5]*5)
        nums.append(num)
        if num == nums[f2]*2:
            f2 += 1
        if num == nums[f3] * 3:
            f3 += 1
        if num == nums[f5]*5:
            f5 += 1

    return nums[target - 1]