def quicksort(arr, low, high):
    if low < high:
        # pi 是经过分区后的枢轴元素的索引，arr[pi]现在放在正确的位置
        pi = partition(arr, low, high)

        # 分别递归地对枢轴左侧和右侧的子数组进行快速排序
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)


def partition(arr, low, high):
    # 选择最后一个元素作为枢轴
    pivot = arr[high]

    # i是小于枢轴元素部分的最后一个元素的索引
    i = low - 1

    for j in range(low, high):
        # 当前元素小于或等于枢轴
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    # 将枢轴元素放到正确的位置
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


import random


def randomized_partition(arr, low, high):
    pivot_index = random.randint(low, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    # 将随机选中的枢轴移到数组末尾
    return partition(arr, low, high)  # 调用标准分区函数


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quicksort(arr, low, high):
    if low < high:
        pi = randomized_partition(arr, low, high)
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)


# 示例用法
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quicksort(arr, 0, n - 1)



import random

def random_select(arr, low, high, k):
    if low == high:
        return arr[low]

    # 随机选择枢轴并对数组进行分区
    pivot_index = random_partition(arr, low, high)
    # 计算枢轴是第几小的元素
    rank = pivot_index - low + 1

    if rank == k:
        return arr[pivot_index]
    elif k < rank:
        return random_select(arr, low, pivot_index - 1, k)
    else:
        return random_select(arr, pivot_index + 1, high, k - rank)
def random_partition(arr, low, high):
    pivot_index = random.randint(low, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    # 将枢轴元素移动到数组末尾
    return partition(arr, low, high)
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

