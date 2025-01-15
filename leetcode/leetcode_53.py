def compute_array_sum(nums):
    result = 0
    for i in range(0, len(nums)):
        result += nums[i]
    return result

    # def maxSubArray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # 方法一，compute all subarrays, this works, but too slow
    '''
    sum = nums[0]
    for i in range(0, len(nums)):
        sub_sum = 0
        for j in range(i, len(nums)):
            sub_sum = compute_array_sum(nums[i: j + 1])
            if sub_sum > sum:
                sum = sub_sum
    return sum
    
    complexity:on^3
    '''

    '''
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        max_num1 = max(nums[0],nums[1])
        max_num2 = nums[0] + nums[1]
        return max(max_num2,max_num1)
    sum = nums[0]
    for i in range(0, len(nums)):
        sub_sum = nums[i]
        sum = max(sum,sub_sum)
        for j in range(i + 1, len(nums)):
            sub_sum += nums[j]

            sum = max(sum, sub_sum)
    return sum
    complexity:on^2
    '''


# 核心逻辑在于，如果current sum 小于零，就可以更新了，因为小于零不会contribute到我们找到最大sum

def maxSubArray(nums):
    max_sub = nums[0]
    current_sum = 0

    for item in nums:
        if current_sum < 0:
            current_sum = 0
        current_sum += item
        max_sub = max(max_sub, current_sum)
    return max_sub


arr1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
arr2 = [-2, -3, -1]
# print(compute_array_sum(arr1))
print(maxSubArray(arr2))


def maxCrossingSum(arr, left, mid, right):
    # 包含中点的左半部分的最大和
    sum = 0
    left_sum = float('-inf')
    for i in range(mid, left-1, -1):
        sum = sum + arr[i]
        if (sum > left_sum):
            left_sum = sum

    # 包含中点的右半部分的最大和
    sum = 0
    right_sum = float('-inf')
    for i in range(mid + 1, right + 1):
        sum = sum + arr[i]
        if (sum > right_sum):
            right_sum = sum
    # 返回跨越中点的子数组的最大和
    return left_sum + right_sum
def maxSubArrayDivideAndConquer(arr, left, right):
    # 基本情况：如果数组只有一个元素
    if (left == right):
        return arr[left]
    mid = (left + right) // 2
    # 返回以下三个中的最大值：
    # 1) 左半部分的最大子数组和
    # 2) 右半部分的最大子数组和
    # 3) 跨越中点的最大子数组和
    return max(maxSubArrayDivideAndConquer(arr, left, mid),
               maxSubArrayDivideAndConquer(arr, mid+1, right),
               maxCrossingSum(arr, left, mid, right))

# 示例用法
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
n = len(arr)
max_sum = maxSubArrayDivideAndConquer(arr, 0, n-1)
print("Maximum contiguous sum is", max_sum)

