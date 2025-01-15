def divide(dividend, divisor):
    is_negative = False
    if dividend < 0 < divisor or dividend > 0 > divisor:
        is_negative = True
    if divisor == 0:
        return 0
    if dividend == divisor or dividend * -1 == divisor:
        return 1 if is_negative is False else -1
    dividend = abs(dividend)
    divisor = abs(divisor)
    count = 0
    while dividend > divisor:
        dividend = dividend - divisor
        count += 1
    return count if is_negative is False else (count*-1)

print(divide(1,-1))
'''
10 - 3 = 7
7 - 3 = 4
4 - 3 = 1 break becase 1 < 3


'''