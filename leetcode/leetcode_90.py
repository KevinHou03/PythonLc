def subsetsWithDup(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    result = []
    nums.sort()

    def backtrack(i, cur):
        if i == len(nums):
            result.append(cur.copy())
            return
        # all subsets that include nums[i]
        cur.append(nums[i])
        backtrack(i + 1, cur)
        cur.pop()
        # all subsets that do not include nums[i]
        while i + 1 < len(nums) and nums[i] == nums[i + 1]:
            i += 1
        backtrack(i + 1, cur)

    backtrack(0, [])
    return result



    backtrack(0, [])
    return result


nums = [1, 2, 3]
print(subsetsWithDup(nums))
