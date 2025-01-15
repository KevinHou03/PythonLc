# 线性查找
def linear_search(sequence, target):
    for i in range(0, len(sequence)):
        if sequence[i] == target:
            return i
    else:  # for-else 结构，
        return None


# 也可以使用enumerate方法，可以同时声明index和其对应的value两个变量,同时还自动遍历整个list
def linear_search_enumerate(sequence, target):
    for index, value in enumerate(sequence):
        if value == target:
            return index
    else:
        return None


# test
sequence1 = [1, 2, 3, 4, 5]

print(linear_search(sequence1, 9))
print(linear_search_enumerate(sequence1, 2))
