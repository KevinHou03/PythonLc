def canPartition(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    # val = sum(nums) // 2
    #
    # def backtrack(index, cur_sum, target):
    #     if cur_sum == target:
    #         return True
    #     if cur_sum > target or index == len(nums):
    #         return False
    #     if backtrack(index + 1, cur_sum + nums[index]):
    #         return True
    #     return backtrack(index + 1, cur_sum)
    #
    # return backtrack(0, 0, val)

    if sum(nums) % 2 == 1:
        return False
    memo = set()
    memo.add(0)
    target = sum(nums) // 2
    for i in range(len(nums) - 1, -1, -1):
        next_memo = set()
        for j in memo: # 你在iterate memo,而同时你准备更新memo,这是不对的，所以要新建一个next_memo
            next_memo.add(j + nums[i])
            next_memo.add(j)
        memo = next_memo
    return True if target in memo else False



