from basic_sorting import exchange


# 记住，一次sink只能纠正一个violation
def sink(sequence, low, high):  # low堆顶，根节点，high是堆尾，最后一个位置
    while 2 * low + 1 <= high:  # high是最底部节点，大于他就越界了，后面没有节点了
        if 2 * low + 2 <= high:
            if sequence[2 * low + 1] > sequence[2 * low + 2]:
                max_index = 2 * low + 1  # 要把最大的换上去
            else:
                max_index = 2 * low + 2
        else:
            max_index = 2 * low + 1
        if sequence[low] > sequence[max_index]:
            break
        exchange(sequence, low, max_index)
        low = max_index
    return sequence


'''
首先把随机数组变成一个heap，然后把首尾元素调换，然后把尾元素
也就是最大的元素，放入辅助数组 然后对第一个元素进行sink
'''


def heap_sort(sequence):
    sequence = heapify(sequence)
    result = []
    while len(sequence) != 0:
        exchange(sequence, 0, len(sequence) - 1)
        result.append(sequence[len(sequence) - 1])
        sequence.pop()
        sink(sequence, 0, len(sequence) - 1)
    return result[::-1]


def heapify(sequence):  # 从有子节点的最后一个节点开始往上遍历 进行sink 即可
    for i in range(len(sequence) // 2, -1, -1):  # 5,4,3,2,1,0
        sink(sequence, i, len(sequence) - 1)
    return sequence


if __name__ == "__main__":
    arr = [1, 3, 8, 7, 5, 9, 5]
    print(heap_sort(arr))
