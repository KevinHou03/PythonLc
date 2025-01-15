def plusOne(digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    if digits[-1] == 9:
        index = len(digits) - 1
        while digits[index] == 9 and index > 0:
            digits[index] = 0
            index -= 1
        if index == 0 and digits[index] == 9:
            digits[index] = 0
            digits.insert(0, 1)
        else:
            digits[index] += 1
    else:
        digits[-1] += 1
    return digits

digits = [8,9,9,9]
print(plusOne(digits))
