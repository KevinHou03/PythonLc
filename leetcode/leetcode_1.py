class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        memo = {}
        for i in range(len(nums)):
            if target - nums[i] in memo:
                return [memo[target - nums[i]], i]
            memo[nums[i]] = i
        return []