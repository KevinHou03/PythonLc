def subsets(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    result = [[]]

    def backtrack(start, cur):
        for i in range(start, len(nums)):
            new_cur = cur + [nums[i]]
            result.append(new_cur)
            backtrack(i + 1, new_cur)

    backtrack(0, [])
    return result


print(subsets([1, 2, 3]))


def subsets2(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    result = []
    subset = []

    def dfs(i):  # current index of the array element we are on
        if i >= len(nums):
            result.append(subset.copy())
            return
        # decision to include num[i]
        subset.append(nums[i])
        dfs(i + 1)
        # decision not to include num[i]
        subset.pop()
        dfs(i + 1)
    dfs(0)
    return result

print(subsets2([1, 2, 3]))