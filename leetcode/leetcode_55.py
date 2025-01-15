'''
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        start = 0
        farthest = 0
        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])
            if farthest >= len(nums) - 1:
                result += 1
                break
            if i == start:
                start = farthest
                result += 1
        return result

'''


def canJump(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    if len(nums) == 1:
        return True
    farthest = 0
    for i in range(0, len(nums) - 1):
        if i > farthest:
            return False
        farthest = max(farthest, i + nums[i])
        if farthest >= len(nums) - 1:
            return True
    return False

nums = [3,2,1,0,4]
print(canJump(nums))