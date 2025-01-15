def remove(nums, val):
    new = []
    for i in range(0, len(nums)):
        if nums[i] != val:
            new.append(nums[i])

    return new


num1 = [3, 2, 2, 3]
print(remove(num1, 3))


def remove2(nums, val):
    k = 0
    for i in range(0, len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    return nums


num2 = [3, 2, 2, 3]
print(remove2(num2, 3))
