from collections import Counter


def canPermutePalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    counter = Counter(s)
    odd = [ch for ch, freq in counter.items() if freq % 2 == 1]
    if len(odd) > 1:
        return False
    return True



s = "code"
print(canPermutePalindrome(s))

