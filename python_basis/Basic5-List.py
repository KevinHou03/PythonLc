# List 列表,是可以混存不同类型的数据的
HKYlIST = ['Hello', 'World', 98]
print(id(HKYlIST))
print(type(HKYlIST))
print(HKYlIST)

# 另一种初始化方法
HKYLIST2 = list(['Hello', "World", 98])

# 有两种索引方式，第一种就是熟知的0，1，2，4... 第二种是从最右边开始从-1起算，-1，-2，-3...
# 以下两种方式应该得到相同的元素
print(HKYlIST[1], HKYlIST[-2])

# 获取特定元素的索引值
print(HKYlIST.index('Hello'))  # 0
print(HKYlIST.index('Hello', 0, 2))  # 查找的元素，起始索引，结束索引

# 切片操作：获取列表中的多个元素，obtain multiple element in one list。
# 切片是左闭右开（。。。]
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list[1:6:1])  # 从左至右start stop step，结果[2, 3, 4, 5, 6],切出来的是一个新的列表
print(list[1:6])  # 默认step是1
print(list[1:6:2])  # [2, 4, 6]

# 当step为负数时，start第一个元素默认为列表最后一个元素，不用写start stop因为默认从最后开始了
print(list[::-1])  # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print(list[::-2])  # [10, 8, 6, 4, 2] 反着打
print(list[6:0:-1])  # [7, 6, 5, 4, 3, 2] 从左边6开始，从右往左因为step为负数，step为1

# 遍历列表
for item in list:
    print(item)

# 列表元素的增删改

List1 = [1, 2, 3, 4, 5]
List1.append(100)  # List1=[1,2,3,4,5,100] 有没有创建新的列表？ 没有，还是原来的列表

List2 = ['hello', 'world', 'NiHao']
List1.append(List2)
print(List1)  # [1, 2, 3, 4, 5, 100, ['hello', 'world', 'NiHao']]
# 如果是List1.extend(List2)，那就是[1, 2, 3, 4, 5, 100,'hello', 'world', 'NiHao']

# append一个list是在列表中加入列表，extend是在列表中加入另外一个列表中的元素。

# insert为在任意索引位置上添加元素
List3 = [1, 2, 3, 4, 5]
List3.insert(2, 'hello')  # 2为索引位置
print(List3)  # [1, 2, 'hello', 3, 4, 5]

# 在任意位置上添加n个元素
List5 = [4, 5, 6, 7, 8, 9, 0]
List4 = [1, 2, 3, 4]
List5[1:] = List4  # 从List5索引1开始全部替换为List4
print(List5)

# 列表元素的删除
'''
remove() 
1.一次只删除一个元素
2.有重复的话删除第一个
3.元素不存在则抛出error
'''
List6 = [1, 2, 3, 4, 5]
List6.remove(3)
print(List6)  # [1, 2, 4, 5]

'''
pop()
1.不指定索引，删除列表最后一个元素
2.指定索引，删除索引元素
3。不存在抛出error
'''
List7 = [1, 2, 3, 4, 5]
List7.pop()
print(List7)  # [1, 2, 3, 4]
List7.pop(3)
print(List7)  # [1, 2, 3]

'''
切片
删除一个元素，但是会产生一个新的列表
因为切片就是产生了一个新列表
'''
List8 = List7[1:3]
print(List8)  # [2, 3]

# 如何删除但是不产生一个新列表？
List7 = [1, 2, 3, 4, 5]
List7[1:3] = []  # 赋空值
print(List7, 'here')

# 清空列表
List7.clear()
print(List7)  # []

"""
修改操作
1.一次修改一个值
"""
List = [1, 2, 3, 4, 5, 6]
List[2] = 100
print(List)  # [1, 2, 100, 4, 5, 6]

List[1:3] = ('Hello', 'World', 'Fuck', 'You')  # [1, 'Hello', 'World', 'Fuck', 'You', 4, 5, 6]
print(List)
