def wiggle_sort_2(nums):
    nums.sort()
    n = len(nums)
    mid = (n + 1) // 2

    sml_half = nums[:mid]
    lrg_half = nums[mid:]

    sml_half.reverse()
    lrg_half.reverse()

    nums[::2] = sml_half
    nums[1::2] = lrg_half

    return nums

nums = [1,5,1,1,6,4]

print(wiggle_sort_2(nums))