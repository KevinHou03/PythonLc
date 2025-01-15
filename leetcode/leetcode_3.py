def aux(s):
    char_list = []
    char_list.append(s[0])
    star = 0
    for i in range(1, len(s)):
        if s[i] in char_list:
            break
        char_list.append(s[i])
        star = i
        print(s[star+1:])

    return len(char_list), s[1:]

def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """






print(aux('pukwswkjew')) # 4

print(lengthOfLongestSubstring("dvdf"))

a = set('pukwswkjew')
print(a)