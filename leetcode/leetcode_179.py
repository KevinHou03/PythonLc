from functools import cmp_to_key

from leetcode.leetcode_75 import sortColors


def largestNumber(nums):
    """
    :type nums: List[int]
    :rtype: str
    """
    for i, val in enumerate(nums):
        nums[i] = str(val)

    def compare(n1, n2): #decide which one goes first makes it the greatest
        if n1 + n2 > n2 + n1:
            return 1
        else:
            return -1

    nums = sorted(nums, key = cmp_to_key(compare))

    return "".join(nums)