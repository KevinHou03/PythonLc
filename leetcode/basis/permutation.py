'''
输入一个列表，生成该列表中所有可能的排列（不允许重复使用元素，排列顺序不同算不同结果）。
'''

def permutaion(nums):

    res = []
    used = [False] * len(nums)
    def backtrack(path):
        if len(path) == len(nums):
            res.append(path[:])
            return

        for i in range(len(nums)):
            if used[i]:
                continue
            used[i] = True
            path.append(nums[i])
            backtrack(path)

            #撤销选择
            path.pop()
            used[i] = False

    backtrack([])
    print(len(res))
    return res


s = [1,2,3,4,5]
print(permutaion(s))

# P(5,5)





