# def intToRoman(num):
#     roman_dict = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L', 90: 'XC', 100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}
#     key_list = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
#     result = []
#     while num != 0:
#         pivot = max(x for x in key_list if x <= num)
#         result.append(roman_dict[pivot])
#         num = num - pivot
#     return "".join(result)
#
# print(intToRoman(1994))


def intToRoman2( num):
    roman_numerals = {
        1000: 'M', 900: 'CM', 500: 'D', 400: 'CD',
        100: 'C', 90: 'XC', 50: 'L', 40: 'XL',
        10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'
    }

    result = ''

    for value, numeral in roman_numerals.items():
        while num >= value:
            result += numeral
            num -= value

    return result

print(intToRoman2(1994))