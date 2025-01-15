


def encrypt(s, n):
    result = []
    for i in range(len(s)):
        if s[i] == " ":
            result.append(" ")
            continue
        value = ord(s[i]) + n
        while value > 122:
            value -= 26
        result.append(chr(value))
    return "".join(result)



def decrypt(s, n):
    result = []
    for i in range(len(s)):
        if s[i] == " ":
            result.append(" ")
            continue
        value = ord(s[i]) - n
        while value < 97:
            value += 26
        result.append(chr(value))
    return "".join(result)


encrypted = encrypt("hello world ",300)
print(encrypted)

print(decrypt(encrypted, 300))
