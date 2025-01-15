def exchange(sequence, a, b):
    temp = sequence[a]
    sequence[a] = sequence[b]
    sequence[b] = temp


'''
# test for exchange()
sequence1 = [1, 2, 3, 4, 5, 6]
exchange(sequence1, 1, 2)
print(sequence1)
'''


# bubbleSort 冒泡排序

def bubble_sort(sequence):
    for i in range(0, len(sequence) - 1):
        swapped = False
        for j in range(0, len(sequence) - 1 - i):
            if sequence[j] > sequence[j + 1]:
                exchange(sequence, j, j + 1)
                # 如果没有exchange方法，也可以写 sequence[j],sequence[j+1] = sequence[j+1], sequence[j]
                swapped = True
        if not swapped:
            break
    return sequence


'''
python中，for i in range(0, len(sequence) - 1):0到len(sequence) - 2 
         for i in (0, len(sequence) - 1): 这是一个tuple，他只包含两个元素，0 和 len(sequence) - 1
'''

# bubble sort test
sequence2 = [5, 4, 3, 2, 1, 0, 34, 56, 22, 46, 3, 77, 32, 4, 88, 2, 7, 33]


# print(bubble_sort(sequence2))


# Selection Sort 一直找最小/最大的数
def selection_sort(sequence):
    sequence_aux = []
    for i in range(0, len(sequence)):
        min_val = min(sequence)
        sequence_aux.append(min_val)
        sequence.remove(min_val)
    return sequence_aux


def selection_sort_advanced(sequence):
    for i in range(len(sequence) - 1):
        min_location = i
        for j in range(i + 1, len(sequence)):  # 从i开始也可以
            if sequence[min_location] > sequence[j]:
                min_location = j
        exchange(sequence, min_location, i)
    return sequence


'''
# selection sort test
print(selection_sort(sequence2))
print(selection_sort_advanced(sequence2))
'''


# insertion sort
def insertion_sort(sequence):
    for i in range(1, len(sequence)):
        tmp = sequence[i]
        j = i - 1
        while j >= 0 and sequence[j] > tmp:
            sequence[j + 1] = sequence[j]
            j -= 1
        sequence[j + 1] = tmp
    return sequence


'''
# test for insertion sort
sequence3 = [5, 4, 3, 2, 1, 0, 34, 56, 22, 46, 3, 77, 32, 4, 88, 2, 7, 33]
print(insertion_sort(sequence3))
'''


def insertion_sort_more(sequence):
    N = len(sequence)
    for i in range(1, N):
        j = i
        while j > 0:
            if sequence[j] < sequence[j - 1]:
                exchange(sequence, j, j - 1)
            j = j - 1
    return sequence


'''
sequence3 = [5, 4, 3, 2, 1, 0, 34, 56, 22, 46, 3, 77, 32, 4, 88, 2, 7, 33]
print(sequence3)
print(insertion_sort_more(sequence3))
'''


# quick sort
def quick_sort(sequence):
    quick_sort2(sequence, 0, len(sequence) - 1)
    return sequence


def quick_sort2(sequence, left, right):
    if left >= right:
        return
    pivot = partition(sequence, left, right, right)  # 先把right设为pivot
    quick_sort2(sequence, left, pivot - 1)
    quick_sort2(sequence, pivot + 1, right)


def partition(sequence, left, right, vital):
    pivot = sequence[vital]
    exchange(sequence, vital, right)  # 先把这个pivot放到最右边
    initialIndex = left
    for i in range(left, right):  # right位置是我们的pivot所以不能被包括进去
        if sequence[i] < pivot:
            exchange(sequence, i, initialIndex)
            initialIndex = initialIndex + 1
    exchange(sequence, right, initialIndex)
    return initialIndex


'''
sequence3 = [5, 4, 3, 2, 1, 0, 34, 56, 22, 46, 3, 77, 32, 4, 88, 2, 7, 33]
print(sequence3)
print(quick_sort(sequence3))
'''
