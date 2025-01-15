def transform(s):
    result = 0
    digits = len(s) - 1
    for char in s:
        integer = ord(char) - ord('0')
        result += integer * (10**digits)
        digits -= 1
    print(result)



transform("123333")