def addBinary(a, b):
    """
    :type a: str
    :type b: str
    :rtype: str
    """
    a = a[::-1]
    b = b[::-1]
    max_len = max(len(a), len(b))
    if len(a) < len(b):
        for i in range(len(b) - len(a)):
            a += "0"
    if len(a) > len(b):
        for i in range(len(a) - len(b)):
            b += "0"

    result = []
    carry = False
    for i in range(max_len):
        if (a[i] == "1" and b[i] == "1") or (b[i] == "1" and a[i] == "1"):
            if carry:
                result.append("1")
            else:
                result.append("0")
            carry = True
        elif (a[i] == "0" and b[i] == "0") or b[i] == "0" and a[i] == "0":
            if carry:
                result.append("1")
                carry = False
            else:
                result.append("0")
        else:  # 1/0 and 0/1
            if carry:
                result.append("0")
            else:
                result.append("1")
        if i == max_len - 1 and carry:
            result.append("1")

    return "".join(result)[::-1]



print(addBinary("1111", "1111"))



# def addBinary(a, b):
#
#     a = a[::-1]
#     b = b[::-1]
#     max_len = max(len(a), len(b))
#     if len(a) < len(b):
#         a += "0" * (len(b) - len(a))
#     if len(a) > len(b):
#         b += "0" * (len(a) - len(b))
#
#     result = []
#     carry = False
#     for i in range(max_len):
#         if (a[i] == "1" and b[i] == "1") or (b[i] == "1" and a[i] == "1"):
#             if carry:
#                 result.append("1")
#             else:
#                 result.append("0")
#             carry = True
#         elif (a[i] == "0" and b[i] == "0") or b[i] == "0" and a[i] == "0":
#             if carry:
#                 result.append("1")
#                 carry = False
#             else:
#                 result.append("0")
#         else:  # 1/0 and 0/1
#             if carry:
#                 result.append("0")
#             else:
#                 result.append("1")
#         if i == max_len - 1 and carry:
#             result.append("1")
#     return "".join(result[::-1])
#
# print(addBinary("1111", "1111"))


