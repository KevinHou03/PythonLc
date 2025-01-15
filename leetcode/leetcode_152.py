def maxProduct(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    # 含有正负数，你不知道一个最小数等一下就变成最大数了,或者最大数一下变最小的了
    res = max(nums)
    curMin = 1
    curMax = 1
    for num in nums:
        max_product = curMax * num
        curMax = max(curMax * num, num, curMin * num)
        curMin = min(curMin*num, curMax * num, num)
        res = max(res, curMax)
    return res

nums = [2,3,-2,4]
print(maxProduct(nums))

