from heap_sort import *

# 有n个数，取到前k大的数

'''
排序，对前k个切片 nlogn+k
'''


def topk_raw(sequence, k):
    sequence.sort(reverse=True)
    return sequence[:k]


test1 = [4, 5, 7, 6, 2, 9, 8]
print(topk_raw(test1, 3))

'''
用heap也行
'''


def topk_heap(sequence, k):
    sequence = heapify(sequence)
    return sequence[::k]


test2 = [4, 5, 7, 6, 2, 9, 8]
print(topk_raw(test1, 5))

'''
heap的另一种用法，先把前k个数拿出来建一个heap
堆顶是最大的数
再把整个列表遍历比堆顶大的就放进去，sink，不大就忽略
complecity nlogk
'''


def topk_advanced(sequence, k):
    sample = sequence[:k]
    heapify(sample)
    for i in range(k + 1, len(sequence)):
        if sequence[i] > sample[0]:
            sample[0] = sequence[i]
            sink(sample, 0, len(sample))
    return sample


test3 = [4, 5, 7, 6, 2, 9, 8, 3, 4, 6, 43, 2, 4, 7, 9, 4, 2, 1]
print(topk_raw(test3, 6))
