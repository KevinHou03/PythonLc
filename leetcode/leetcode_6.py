def convert(s, numRows):
    """
    :type s: str
    :type numRows: int
    :rtype: str
    """
    list_set = []

    for i in range(0, numRows):
        sub_list = []
        list_set.append(sub_list)
    # 现在list set里面有n个list，每个list要append相应的char
    i = 0
    while i < len(s):
        for j in range(0, numRows):
            if i < len(s):
                list_set[j].append(s[i])
                i = i + 1
        for k in range(numRows - 2, 0, -1):
            if i < len(s):
                list_set[k].append(s[i])
                i = i + 1
    print(list_set)
    new_list = []
    for element in list_set:
        element = "".join(element)
        new_list.append(element)
    return "".join(new_list)


convert("PAYPALISHIRING", 3)
