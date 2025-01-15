def threeSum(nums):
    result1 = []
    for i in range(0, len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                if nums[i] + nums[j] + nums[k] == 0:
                    result = [nums[i], nums[j], nums[k]]
                    result1.append(result)
    unique_list = list(set(tuple(sorted(sublist)) for sublist in result1))
    return unique_list


print(threeSum([-1, 0, 1, 2, -1, -4]))
print(threeSum([0,0,0]))
