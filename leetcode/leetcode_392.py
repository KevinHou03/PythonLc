def isSubsequence(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    p1, p2 = 0,0

    while p1 < len(s) and p2 < len(t):
        if s[p1] == t[p2]:
            p1 += 1
        p2 += 1
        
        if p1 == len(s):
            return True

    return False

print(isSubsequence("abcd", "ahbgdc"))
