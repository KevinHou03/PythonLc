def longestConsecutive(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    #使用·set， 因为set中的增删改都是O（1）
    num_set = set(nums)
    ans = 0

    for num in nums:
        if num - 1 not in num_set: # it is a sequence-start
            length = 1
            while num + 1 in num_set:
                length += 1
                num += 1
            ans = max(length, ans)
    return ans



nums = [100,4,200,1,3,2]
print(longestConsecutive(nums))

def dp(nums2):
    """
    key：数组中的某个数字
    value：包含num的连续序列的总长度
    """

    dp = {}
    longest = 0

    for num in nums2:
        if num not in dp:
            left_len = dp.get(num - 1, 0)
            right_len = dp.get(num + 1, 0)

            length = left_len + right_len + 1
            dp[num] = length

            dp[num - left_len] = length
            dp[num + right_len] = length

            longest = max(longest, length)
    return longest

nums2 = [100,4,200,1,3,2]
print(dp(nums2))

