def singleNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    dict = {}
    for num in nums:
        if num in dict:
            dict[num] += 1
        else:
            dict[num] = 1

    return [key for key, value in dict.items() if value == 1][0]

nums = [2,2,1]
print(singleNumber(nums))


def better(nums):
    result = 0
    for num in nums:
        result ^= num  # XOR all numbers
    return result

"""
x⊕x=0 (a number XORed with itself is 0).
x⊕0=x (a number XORed with 0 is itself).
XOR is commutative and associative, so the order of operations doesn't matter.

When all numbers are XORed together, the pairs cancel out (because 
𝑥
⊕
𝑥
=
0
x⊕x=0), leaving only the single number.
Time complexity: 
𝑂
(
𝑛
)
O(n) (single pass through nums).

"""