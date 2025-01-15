def productExceptSelf(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    res = [1] * len(nums)
    pre_product = 1
    for i in range(len(nums)):
        res[i] = pre_product
        pre_product *= nums[i]

    post_product = 1
    for i in range(len(nums) - 1, -1, -1):
        res[i] *= post_product
        post_product *= nums[i]

    return res


print(productExceptSelf([1, 2, 3, 4]))