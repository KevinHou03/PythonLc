# 二分查找法，从中间开始找，前提是列表必须有序


def binary_search(sequence, target):
    left = 0
    right = len(sequence) - 1
    while left <= right:
        mid = (left + right) // 2
        if sequence[mid] == target:
            return mid
        elif sequence[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    else:
        return None


sequenceTest = [1, 2, 3, 5, 6, 7, 9, 16, 48]
print(binary_search(sequenceTest, 7))
