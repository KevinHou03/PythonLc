
# 这道题问的是：给定的s里的全部letters可以任由组合的话，可以生成几个palindromes
'''
所以
1 要组成pa， 必须要保证的是，在偶数长度的回文中，所有字符出现次数都为偶数；在奇数长度的回文中，只有 1 个字符出现奇数次，其他都为偶数次
2 如果有一个以上letter出现了奇数次，则return false，不能组成任何pa
3 只要有一个字符出现了奇数次，则把它记录到 mid，作为回文的中间字符
4 如果某个字符出现了奇数次（比如出现了 3 次、5 次……），我们会将它的一部分放入「half」、把「多出来的那一个」放到 mid 里

'''
from collections import Counter


def generatePalindromes_subsequence(s):

    # 1. count
    count = Counter(s) # Counter({'a': 2, 'b': 2})
    # 2. 判断是否有超过一个letter出现了奇数次
    odd_char = [ch for ch, freq in count.items() if freq % 2 == 1] # 这个list全是出现奇数次的letter
    if len(odd_char) > 1:
        return []


    # mid 永远只有一个char, 不可能出现多个，要不然pa无法形成
    half, mid = [], ""
    for ch, freq in count.items():
        if freq % 2 == 1:
            mid = ch
        half.extend(ch * (freq // 2)) # extend把元素逐一添加，append会把他们作为一个新list加进去

    ans = []

    # 对half进行permutation find all possible permutation, which means in this case the order matters

    def backtrack(halve, used, path):

        # base case
        if len(halve) == len(path): # all chars are used, a new permutation generated
            left = "".join(path)
            ans.append(left + mid + left[::-1])

        for i in range(len(halve)):
        # 若已用过或和前一个相同且前一个还没用，则跳过（去重）
            if used[i]:
                continue
            if i > 0 and half[i] == half[i - 1] and not used[i - 1]:
                continue
            used[i] = True
            path.append(half[i])
            backtrack(halve, used, path)
            path.pop()
            used[i] = False

    half.sort()
    used = [False] * len(half)

    backtrack(half, used, [])
    return ans


s = "aabb"
print(generatePalindromes_subsequence(s))


'''
为什么需要 used？
在生成全排列时，如果 half 里有重复字符（例如 ['a','a','b']），我们要确保不会生成重复的排列。常用做法是：

遍历所有位置 i，若 used[i] == True 表示第 i 个字符已被放进当前排列（path）里了，就不能再用它一次。
去重技巧：如果本轮要用的字符 chars[i] 与前一个字符 chars[i-1] 相同，而且前一个还没用（used[i-1] == False），则说明会产生重复路径，需要 continue 跳过。
因此，used 数组配合「相邻重复字符」判断，能保证同一层递归中，相同字符只会被使用一次，不会生成重复排列
'''
