def permute(nums):
    result_list = []
    nums = sorted(nums)
    used = [False] * len(nums)
    backtrack(nums,result_list,[],used)
    return result_list


def backtrack(nums, result_list, temp_list,used):
    # base case: 如果temp_list的长度和原nums长度相同了，就用result append他
    if len(temp_list) == len(nums):
        result_list.append(temp_list[:])
        return
    for index, element in enumerate(nums):
        # skip this number if its already used
        # if element in temp_list:
        #     continue
        # if not, add it to the temp list
        if used[index]:
            continue
        if index > 0 and nums[index] == nums[index - 1] and not used[index - 1]:
            continue
        temp_list.append(element)
        used[index] = True
        # go back (backtracking) to try another number
        backtrack(nums, result_list, temp_list[:],used)
        temp_list.pop()
        used[index] = False


print(permute([1,2,1]))
