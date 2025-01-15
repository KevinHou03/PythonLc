def combinationSum(candidates, target):
    """
    :type candidates: List[int]
    :type target: int
    :rtype: List[List[int]]
    """

    def dfs(start, current_combination, target):
        if target == 0:
            temp = current_combination
            result.append(temp[:])
        for i in range(start, len(candidates)):
            if target < candidates[i]:
                break
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            current_combination.append(candidates[i])
            dfs(i, current_combination, target - candidates[i])
            current_combination.pop()

    result = []
    candidates.sort()
    dfs(0, [], target)
    return result


candidates1 = [2, 3, 6, 7]
target1 = 7
print(combinationSum(candidates1, target1))


def combinationSum(self, candidates, target):
    ret = []
    self.dfs(candidates, target, [], ret)
    return ret


def dfs(self, nums, target, path, ret):
    if target < 0:
        return
    if target == 0:
        ret.append(path)
        return
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:
            continue  # Skip duplicates
        self.dfs(nums[i + 1:], target - nums[i], path + [nums[i]], ret)


candidates = [1, 2, 3]
target = 4


# Initial call: self.dfs(candidates, target, [], ret)
# Loop 1: self.dfs([1, 2, 3], 4, [], ret)
#   Loop 1.1: self.dfs([1, 2, 3], 3, [1], ret)
#     Loop 1.1.1: self.dfs([1, 2, 3], 2, [1, 1], ret)
#       Loop 1.1.1.1: self.dfs([1, 2, 3], 1, [1, 1, 1], ret)
#         Loop 1.1.1.1.1: self.dfs([1, 2, 3], 0, [1, 1, 1, 1], ret) - Adds [1, 1, 1, 1] to ret
#       Loop 1.1.1.2: self.dfs([1, 2, 3], 0, [1, 1, 1, 2], ret) - Adds [1, 1, 1, 2] to ret
#       Loop 1.1.1.3: self.dfs([1, 2, 3], -1, [1, 1, 1, 3], ret) - Skips due to target < 0
#     Loop 1.1.2: self.dfs([1, 2, 3], 1, [1, 2], ret)
#       Loop 1.1.2.1: self.dfs([1, 2, 3], -1, [1, 2, 2], ret) - Skips due to target < 0
#     Loop 1.1.3: self.dfs([1, 2, 3], 0, [1, 3], ret) - Adds [1, 3] to ret
#   Loop 1.2: self.dfs([2, 3], 2, [2], ret)
#     Loop 1.2.1: self.dfs([2, 3], 0, [2, 2], ret) - Adds [2, 2] to ret
#   Loop 1.3: self.dfs([3], 1, [3], ret)
#     Loop 1.3.1: self.dfs([3], -2, [3, 3], ret) - Skips due to target < 0
# Loop 2: self.dfs([2, 3], 3, [], ret)
#   Loop 2.1: self.dfs([2, 3], 1, [2], ret)
#     Loop 2.1.1: self.dfs([2, 3], -1, [2, 1], ret) - Skips due to target < 0
#   Loop 2.2: self.dfs([3], 2, [3], ret)
#     Loop 2.2.1: self.dfs([3], 0, [3, 3], ret) - Adds [3, 3] to ret
# Loop 3: self.dfs([3], 0, [], ret) - Adds [] to ret

def combinationSum2(candidates, target):
    def dfs(start, current_combination, target):
        if target == 0:
            result.append(current_combination[:])
            return
        for i in range(start, len(candidates)):
            if target < candidates[i]:
                break
            # Skip duplicates by starting from the current index
            # if i > start and candidates[i] == candidates[i - 1]:
            #     continue
            current_combination.append(candidates[i])
            dfs(i + 1, current_combination, target - candidates[i])
            current_combination.pop()

    result = []
    candidates.sort()  # Sort the candidates at the beginning
    dfs(0, [], target)
    return result


candidates2 = [2, 3, 6, 7]
target2 = 7
print(combinationSum2(candidates2, target2))