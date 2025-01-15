def remove(num):
    for i in range(0, len(num) - 1):
        if num[i] == num[i + 1]:
            j = i
            while num[i] == num[j]:
                j += 1
            print(i, j - 1)

            # for k in range(j, len(num) - 1):
            #     num[k] = num [k + 1]
    return num


num1 = [1, 1, 1, 3, 4, 5, 5]


# 5print(remove(num1))


def remove2(num):
    available = 1
    for i in range(1, len(num)):
        if num[i] != num[i - 1]:
            num[available] = num[i]
            available += 1
    return num


# num2 = [1, 1, 1, 3, 4, 5, 5]
# print(remove2(num2))


def remove3(num):
    left = 0
    right = 1
    while right < len(num):
        while right < len(num) and num[right] == num[left]:
            right += 1

        if right < len(num):
            left += 1
            num[left] = num[right]

        left += 1
        right += 1

        return num


#
# num3 = [1, 1, 1, 3, 4, 5, 5, 6]
# print(remove3(num3))

def remove4(nums):
    new = []
    for i in range(0, len(nums)):
        if nums[i] not in new:
            new.append(nums[i])
    return new


num3 = [1, 1,2]
print(remove4(num3))


s1 = 'bbab'
s2 = 'chfnebbabjfejf'
bo = s1 in s2
print(bo)
