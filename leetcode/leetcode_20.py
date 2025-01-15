def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    result = []
    for element in s:
        if element in '({[':
            result.append(element)
        elif element in ')}]':
            if len(result) == 0:
                return False
            elif result.pop() != '({['[')}]'.index(element)]:
                return False
    return len(result) == 0

print(isValid('()'))

