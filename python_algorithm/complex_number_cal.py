def cal(a, b, c, d):
    para1 = a * c
    para2 = b * d
    para3 = (a + b) * (c + d)
    real_part = para1 - para2
    imaginary_part = para3 - para1 - para2

    return real_part, imaginary_part


print(cal(9, -3, 3, -9))
