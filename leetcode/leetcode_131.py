def partition(s):
    """
    :type s: str
    :rtype: List[List[str]]
    """
    result = []
    def is_palindrome(s):
        return s == s[::-1]

    def backtrack(start, path):

        if start == len(s):
            result.append(path[:]) # 必须添加的是副本：path[:]而不是path，因为这样path后续更改才不会影响result
            return

        for end in range(start + 1, len(s) + 1):
            sub = s[start:end]
            if is_palindrome(sub):
                path.append(sub)
                backtrack(end, path)
                path.pop()

    backtrack(0,[])
    return result


s = "aab"

print(partition(s))