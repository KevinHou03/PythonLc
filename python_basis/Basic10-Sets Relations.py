"""
集合之间的关系
1.判断相等，元素相同即相等，顺序不重要
2.判断子集
3.判断超集
4.判断交集 False 代表有交集，True代表没交集，disjoint
5.交集
6.并集
7.差集，即两个集合做减法
8.对称差集
"""
# 1.
s1 = {10, 20, 30, 40}
s2 = {20, 30, 10, 40}
print(s1 == s2)  # True

# 2（3）.
s1 = {10, 20, 30, 40, 50, 60}
s2 = {10, 20, 30, 40}
s3 = {10, 20, 90}
print(s2.issubset(s1))  # True
print(s3.issubset(s1))  # Falsw

print(s1.issuperset(s2))  # True
print(s1.issuperset(s3))  # False

# 4.
print(s1.isdisjoint(s2))  # False
s4 = {1, 2, 3}
print(s4.isdisjoint(s1))  # True

# 5交集
s1 = {10, 20, 30, 40, 50, 60}
s2 = {10, 20, 30, 40}
s3 = {10, 20, 90}
print(s1.intersection(s2))  # {40, 10, 20, 30}
print(s1 & s2)  # {40, 10, 20, 30}

# 6并集
print(s1.union(s3))  # {40, 10, 50, 20, 90, 60, 30}
print(s1 | s3)  # {40, 10, 50, 20, 90, 60, 30}

# 7 差集
print(s1.difference(s2))  # {50, 60}
print(s1 - s2)  # {50, 60}

# 8.对称差集
print(s1.symmetric_difference(s2))  # {50, 60}
print(s1 ^ s2)  # {50, 60}
