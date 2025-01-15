def str_str(sub, Str):
    for i in range(0, len(Str)):
        if Str[i] == sub[0]:
            if Str[i:len(sub) + i] == sub:
                return i
    return -1


s1 = 'abcbed'
s2 = 'be'
print(str_str(s2,s1))