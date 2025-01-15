def encrypt(s, a, b):
    result = []
    for i in range(0, len(s)):
        if s[i] == " ":
            result.append(" ")
            continue
        value = ((ord(s[i]) - 97) * a + b) % 26
        char = chr(value + 97)
        result.append(char)
    return "".join(result)





def find_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        x, y, z = find_gcd(b % a, a)
        return x, z - (b // a) * y, y


def find_inverse(a):
    g, x, y = find_gcd(a, 26)
    return x % 26


def decrypt(s, a, b):
    a_inv = find_inverse(a)
    result = []
    for i in range(len(s)):
        if s[i] == " ":
            result.append(" ")
            continue
        value = ((ord(s[i]) - 97 - b) * a_inv) % 26
        char = chr(value + 97)
        result.append(char)
    return "".join(result)

encrypt = encrypt("hello emory hello world", 9, 3)
print(encrypt)
print(decrypt(encrypt, 9, 3))
