import math


def getFactors(n):
    """
    :type n: int
    :rtype: List[List[int]]
    """
    ans = []

    def backtrack(cur_val, path, start):
        if cur_val == 1 and path:
            ans.append(path[:])
            return

        i = start
        while i * i <= cur_val:
            if cur_val % i == 0:
                path.append(i)
                backtrack(cur_val // i, path, i)
                path.pop()
            i += 1

        if cur_val >= start and cur_val != n:
            path.append(cur_val)
            ans.append(path[:])
            path.pop()

    backtrack(n, [], 2)
    return ans


print(getFactors(12))

def getFactors2(n):
    """
    :type n: int
    :rtype: List[List[int]]
    """

    def backtrack(cur_val, path):
        if path:
            ans.append(path + [cur_val])
        for i in range(2, int(math.sqrt(cur_val)) + 1):
            if cur_val % i == 0: # 现在i是我们找到的一个factor，我们要判断他是否合法
                if not path or i >= path[-1]: # # 确保 i >= path[-1] 避免重复组合（保证非递减）
                    backtrack(cur_val // i, path + [i])
    ans = []
    backtrack(n, [])
    return ans



print(getFactors2(12))
'''
在「因数分解」或「组合求解」这类问题中，“保证非递减”通常指 **组合中的元素值依次不变或增加**，用数学术语说，
就是 a1 < a2 < a3...这样做的直接好处是，可以"避免在结果中出现相同元素但顺序不同的重复解"。
'''