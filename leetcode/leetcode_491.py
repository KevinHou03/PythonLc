def findSubsequences(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """

    res = []
    def backtrack(start, path):
        if len(path) >= 2:
            res.append(path[:])
        used_num = set() # 去重,避免出现重复的答案 同层去重
        for i in range(start, len(nums)):
            if nums[i] in used_num:
                continue
            if not path or nums[i] >= path[-1]:
                used_num.add(nums[i])
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()

    backtrack(0, [])
    return res


nums = [4,6,7,7]
print(findSubsequences(nums))