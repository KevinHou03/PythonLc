from leetcode.leetcode_61 import current


def findSubstringInWraproundString(s):
    """
    :type s: str
    :rtype: int
    """

    dp = [0] * 26

    current_len = 0
    for i in range(len(s)):
        if i > 0 and (ord(s[i]) - ord(s[i - 1]) == 1 or (s[i] == 'a' and s[i - 1] == 'z')):
            current_len += 1
        else:
            current_len = 1

        index = ord(s[i]) - ord('a')
        dp[index] = max(dp[index], current_len)

    return sum(dp)

