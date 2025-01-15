def generatePossibleNextMoves(currentState):
    """
    :type currentState: str
    :rtype: List[str]
    """
    if "++" not in currentState:
        return []
    ans = []
    for i in range(len(currentState) - 1):
        if currentState[i] == "+" and currentState[i + 1] == "+":
            ans.append(currentState[:i] + "--" + currentState[i+2:])
    return ans


s = "---+++-+++-+"
print(generatePossibleNextMoves(s))


def twoSum(nums, target):
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


nums = [2,7,11,15]
target = 9

print(twoSum(nums, target))