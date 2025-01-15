'''
输入一个列表和一个整数k，生成该列表中所有大小为𝑘的组合。
'''

def combinations(n, k):
    res = []

    def backtrack(start, path):
        if len(path) == k:
            res.append(path[:])
            return

        for i in range(start, len(n) + 1):
            path.append(i)
            backtrack(i + 1, path)
            path.pop()

    backtrack(0, [])
    return res

nums = [1, 2, 3, 4]
k = 2
print(combinations(nums, k))