def find_reverse(s):
    s = 'abc'
    s = s[::-1]
    print(s)


def find_all_palindrome(s):
    if len(s) < 2:
        return s
    palindrome_list = []
    for index, char in enumerate(s):
        for sub_index in range(index + 1, len(s)):
            if s[sub_index] == s[index]:
                sub_str = s[index:sub_index + 1]
                if sub_str == sub_str[::-1]:
                    palindrome_list.append(sub_str)
    max_len = 0
    max_str = ""
    for element in palindrome_list:
        if len(element) > max_len:
            max_str = element
            max_len = len(max_str)

    if len(palindrome_list) == 0:
        return s[0]
    return max_str

print(find_all_palindrome('CCC'))