# 排序

List = [13, 8, 75, 9, 91, 58, 8]
List.sort()
print(List)  # 排序在原列表的基础上排序的，没有建立一个新列表

# 降序排列
List.sort(reverse=True)
print(List)  # 排序在原列表的基础上排序的，没有建立一个新列表

# 在建立一个新列表的基础上进行排列
List = [13, 8, 75, 9, 91, 58, 8]
ListNew = sorted(List)
print(List)
print(ListNew)

# 降序
ListNew2 = sorted(List, reverse=True)
print(ListNew2)

# 列表自动生成式
ListGenerate = [i for i in range(1, 10)]
print(ListGenerate)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

ListGenerate = [i * i for i in range(1, 10)]
print(ListGenerate)  # [1, 4, 9, 16, 25, 36, 49, 64, 81]

# Exercise: 生成2，4，6，8，10
ListTest = [2 * i for i in range(1, 6)]
print(ListTest)
