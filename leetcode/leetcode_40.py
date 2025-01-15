def combinationSum2(self, candidates, target):
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