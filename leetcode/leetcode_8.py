def myAtoi(s):
    """
    :type s: str
    :rtype: int
    """
    is_neg = False
    int_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    temp = []
    for i in range(len(s)):
        if s[i] == "-":
            is_neg = True
        if s[i] in int_list:
            temp.append(s[i])
    str1 = "".join(temp)
    int1 = int(str1)
    if is_neg:
        return int1 * -1
    else:
        return int1


print(myAtoi("words and 987"))
