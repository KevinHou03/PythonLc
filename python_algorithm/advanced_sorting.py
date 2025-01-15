'''
mergesort
'''
from basic_sorting import exchange

import sys

sys.setrecursionlimit(99)


def merge(List, low, mid, high):
    i = low
    j = mid + 1
    tmp = []
    count = 0
    while i <= mid and j <= high:  # 只要左右两边都有数
        if List[i] <= List[j]:
            tmp.append(List[i])
            i += 1
        else:
            tmp.append(List[j])
            j += 1
            count += (mid - i + 1)
    while i <= mid:  # 第一部分还有数
        tmp.append(List[i])
        i += 1
    while j <= high:  # 右边第二部分还有数
        tmp.append(List[j])
        j += 1
    List[low:high + 1] = tmp
    return count


def merge_sort(List, low, high):
    total_count = 0

    if low < high:
        mid = (low + high) // 2
        # 递归地对左半部分进行归并排序，并获取左半部分的逆序对数量
        left_list, left_count = merge_sort(List, low, mid)
        # 递归地对右半部分进行归并排序，并获取右半部分的逆序对数量
        right_list, right_count = merge_sort(List, mid + 1, high)
        # 合并左右两个有序数组，并计算合并后的逆序对数量
        combined_count = merge(List, low, mid, high)
        # 计算总的逆序对数量
        total_count = left_count + right_count + combined_count
    else:
        # 如果 low 和 high 相等，说明只有一个元素，此时逆序对数量为 0
        total_count = 0
    return List, total_count

# 测试
test1 = [2, 3, 8, 6, 1]
sorted_list, inversions = merge_sort(test1, 0, len(test1) - 1)
print("mergesort:", sorted_list, "逆序对数量:", inversions)


'''
ShellSort 希尔排序
对于长度是n的列表
d1 = n/2 将元素分为d1个组，每组相邻两个元素间隔为d1，对每组插入排序
d2 = d1/2 将元素分为d2个组，每组相邻两个元素间隔为d2，对每组插入排序
......

对于每一个间隔dn,分成dn组，对于每组进行排序
这种方法每一趟不会使某些元素有序，但是会让数据整体趋于有序，最后一趟使所有数据有序
'''


def insertion_sort_gap(List, gap):
    for i in range(gap, len(List)):
        temp = List[i]
        j = i - gap
        while j >= 0 and List[j] > temp:
            List[j + gap] = List[j]
            j -= gap
        List[j + gap] = temp
    return List


def shell_sort(List):
    d = len(List) // 2
    while d >= 1:
        insertion_sort_gap(List, d)
        d //= 2
    return List


# test
list1 = [7, 6, 5, 4, 3, 2, 1]
print(shell_sort(list1))

'''
计数排序,要求已知最大值
'''


def count_sort(List, max_count=100):
    count = [0 for _ in range(max_count + 1)]
    # 表示对这个迭代器进行遍历，遍历的每个元素都用占位符 _ 表示，因为在循环体内不需要使用这个元素的值# 创造一个长度为n的列表：my_list = [i for i in range(n)]
    for value in List:  # 指向里面的每一个数字
        count[value] += 1
    List.clear()  # 把list清空
    for index, value in enumerate(count):
        for i in range(0, value):
            List.append(index)
    return List


list1 = [7, 6, 5, 4, 3, 2, 1]
print(count_sort(list1))

'''
桶排序
在countsort基础上，如果数值范围比较大就不好用了
这样我们就做桶子，每个桶子是一个范围
'''


def bucket_sort(List, n=100, MAX=10000):  # 把最大为10000的数分到100个桶里,一个桶里100个数，也就是MAX / n
    buckets = [[] for _ in range(n)]  # 和上一个一样初始化一个二维数组，外层数组里有一共n个内层数组
    for var in List:
        bucketNum = MAX / n  # 100
        key = min(var // bucketNum, n - 1)  # 这是决定var这个数字放在几号桶里
        # 这里用min是考虑特殊情况 var = 10000, 只有99个桶，10000只能放进99号桶里
        # 放进去的过程中排序：
        buckets[key].append(var)
        for j in range(len(buckets[key]) - 1, 0):
            if buckets[key][j] < buckets[key][j - 1]:
                exchange(buckets[key], j, j - 1)
            else:
                break  # 有一个比他小，就可以跳出去
        # 目前每个桶里有序，且所有元素已经放入桶中
        result = []
        for Bin in buckets:
            result.extend(Bin)  # The extend() method in Python is used to add elements from an iterable (e.g.,
            # a list, tuple,or another iterable object
        return result

    List1 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    print(bucket_sort(List1, 100, 10000))


'''
基数排序，按照digit排序
'''


def radix_sort(List):
    max_num = max(List)  # 88-两次 8888-四次 999999-六次
    max_digit = len(str(max_num))
    count = 0
    while count < max_digit:
        # 创建10个桶，每个桶一位数 0 - 9
        buckets = [[] for _ in range(10)]
        for var in List:
            digit = (var // (10 ** count)) % 10
            buckets[digit].append(var)
        # 分桶完成
        List.clear()
        for buc in buckets:
            List.extend(buc)
        count += 1  # 这就又分桶，直至count = max_digit
    return List


List1 = [999, 7, 66, 36, 366, 3224, 75, 553, 74, 6, 33]
print(radix_sort(List1))
