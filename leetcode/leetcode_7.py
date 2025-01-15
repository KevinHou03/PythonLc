def reverse_integer(x):
    digit_list = []
    if x < 0:
        x = -1 * x
    int_len = len(str(x))
    for i in range(0, int_len):
        quotient = x // 10 ** (int_len - 1)
        remainder = x % 10 ** (int_len - 1)
        digit_list.append(quotient)
        x = remainder
        int_len -= 1
    digit_list.reverse()
    number = int(''.join(map(str, digit_list)))

    if number <= -2**31 or number >= 2**31:
        return 0

    return number


print(reverse_integer(1234567899999999999))