def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    roman_list = list(s)
    print(roman_list)
    sum = 0
    # addition = True
    # for i in range(0, len(roman_list) - 1):
    #     if roman_dict[roman_list[i]] >= roman_dict[roman_list[i + 1]]:
    #         addition = True
    #     else:
    #         addition = False
    #         break
    # if addition:
    #     for char in roman_list:
    #         sum = sum + roman_dict[char]
    # if not addition:

    pre = 0
    post = pre + 1
    # for i in range(0, len(roman_list) - 1):
    while pre <= len(roman_list) - 1:  # pre <= 4
        if pre >= len(roman_list) - 1:
            return sum + roman_dict[roman_list[pre]]
        print(pre)
        if roman_dict[roman_list[pre]] >= roman_dict[roman_list[post]]:
            sum = sum + roman_dict[roman_list[pre]]
            pre = pre + 1
            post = pre + 1

        if pre >= len(roman_list) - 1:
            return sum + roman_dict[roman_list[pre]]

        if roman_dict[roman_list[pre]] < roman_dict[roman_list[post]]:
            if pre >= len(roman_list) - 1:
                return sum + roman_dict[roman_list[pre]]
            temp_sum = roman_dict[roman_list[post]] - roman_dict[roman_list[pre]]
            sum = sum + temp_sum
            pre = pre + 2
            post = pre + 1

    return sum


print(romanToInt("MCMXCIVV"))
# 1000 100 1000 10 100 1 5

'''
0 1: 1000
1 2 1900 
3 4 90

'''
