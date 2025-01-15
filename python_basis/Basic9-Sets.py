"""
集合（set）是python的内置结构
可变,但是集合中的元素不允许重复，如果有重复，它自动合并为一个
属于是没有value的字典（dict）
字典和集合都是用大括号创建的，但不同的是字典是paired，集合是singled
"""
# 创建方式一：
s1 = {'Hello', 'Python', 5, 5, 8, True}
print(s1)  # {True, 5, 'Hello', 8, 'Python'} order changed because it is already processed by the hash function.

# 创建方式二：
s2 = set(range(6))
print(s2)  # {0, 1, 2, 3, 4, 5}

# 创建方式三：
s3 = set([1, 2, 3, 3, 3, 3, 4, 5, ])  # s3=set([1,2,3,3,3,3,4,5,]) 与 s3= set(1,2,3,3,3,3,4,5,)是一样的
print(s3)  # {1, 2, 3, 4, 5} 不允许重复

# 创建空集合
s4 = {}  # 此为空字典
s5 = set()  # 此为空字典

"""
集合的相关操作
1.in/not in
2.添加，add()一次加一个 update()一次至少加一个
3.删除
"""

# 1.
s8 = {10, 20, 'Fuck', False, 98}
print(10 in s8)
print(20 not in s8)
print(22 in s8)

# 2.
s8.add(88)
print(s8)  # {False, 98, 10, 'Fuck', 20, 88}

s8.update({200, 'Shit', True})  # update() 一次加上另一个list/set/tuple
print(s8)  # {False, 'Fuck', 98, 'Shit', True, 200, 10, 20, 88}

s8.update([1, 2, 3, 4, 'Hey'])  # update一个list
s8.update((83, 83, 94))  # update一个tuple
print(s8)

# 3.
s8.remove(100)
s8.remove(False)
# 如果删除的元素不存在，结果抛异常，如果不想要抛异常，这用discard()
s8.discard('Kevin NB ')
# pop(),不需要任何参数，直接删除第一个元素（左边第一个元素）
s8.pop()

s8.clear()  # 清空
