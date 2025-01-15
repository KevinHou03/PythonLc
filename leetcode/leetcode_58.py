def remove_ending_space(s):
    if s[-1] != " ":
        return s
    s = s[:len(s) - 1]
    return remove_ending_space(s)

s2 = "hsd   "
print(remove_ending_space(s2))



def lengthOfLastWord(s):
    """
    :type s: str
    :rtype: int
    """
    target = 0
    if s[-1] == " ":
        s = remove_ending_space(s)
    for i in range(len(s) - 1, -1, -1):
        if s[i] == " ":
            target = i + 1
            break
    return len(s[target:])




s1 ="    fly me   to   the moon "
print(lengthOfLastWord(s1))


