def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    result = []
    index = 0
    first_ele = strs[0]
    for i in range(0, len(first_ele)):
        flag = True
        for j in range(1, len(strs)):
            if i > len(strs[j]) - 1 or first_ele[i] != strs[j][i]:
                return "".join(result)
            # if first_ele[i] != strs[j][i]:
            #     # result.append(first_ele[i])
            #     flag = False
            #     return "".join(result)
        if flag:
            result.append(first_ele[i])
    return "".join(result)

print(longestCommonPrefix(["cir", "car"]))
