"""
字典（Hash）：python内置数据结构，与列表一样是一个可变序列，但是他是无序的
[]是列表，{}是字典
列表是一个一个元素储存的，而字典是一对一对储存的
"""

# 第一种创建方式
scores = {'Kevin': 100, 'Jack': 98, 'Harry': 87}
print(scores)
print(type(scores))  # <class 'dict'>

# 第二种创建方式：
student = dict(name='Jack', age=20)
print(student)

# 创建空字典
d = {}
print(d)

# 如何获取字典中元素？

# 第一种：
print(scores['Jack'])  # 98
# 第二种：
print(scores.get('Harry'))  # 87
# 二者区别：如果查找物不存在，第一种报错为key-error，第二种get不会报错，只会print None

print(scores.get('Lucas', 666))  # 此为在该值不存在时输出666。

# 对于key的判断，使用in 和 not in
print('Kevin' in scores)  # True
print('Harry' not in scores)  # False

# 删除 del=delete 注意用[] 这个一删就删一对 value-key pair
del scores['Kevin']
print(scores)  # {'Jack': 98, 'Harry': 87}

# scores.clear()清空字典所有元素

# 添加：
scores['Zilu'] = 84

# 修改
scores['Zilu'] = 85

# 获取字典视图： keys() valus() item()<——两个都获得
scores = {'Kevin': 100, 'Jack': 98, 'Harry': 87}
print(scores["Kevin"])  # l另外一种获取key-value的方法
key1 = scores.keys()
print(key1)  # dict_keys(['Kevin', 'Jack', 'Harry'])
print(type(key1))  # <class 'dict_keys'> 一个key的列表

values1 = scores.values()
print(values1)  # dict_values([100, 98, 87])
print(type(values1))  # <class 'dict_values'>

items1 = scores.items()
print(items1)  # dict_items([('Kevin', 100), ('Jack', 98), ('Harry', 87)])
print(type(items1))  # <class 'dict_items'>

# 元组，转换之后的2列表是由元组组成的。[()]
print(list(items1))  # [('Kevin', 100), ('Jack', 98), ('Harry', 87)]

# 字典的遍历，依次获取字典里面的元素
for item2 in scores:
    print(item2)  # 获取的是key

for item2 in scores:
    print(scores[item2])  # 获取的是value

# key不能重复，value可以重复，key是唯一的

# 字典生成式
items = ['apple', 'banana', 'grape']
prices = [12, 34, 56]

d = {item.upper(): price for item, price in zip(items, prices)}
print(d)  # {'APPLE': 12, 'BANANA': 34, 'GRAPE': 56}
