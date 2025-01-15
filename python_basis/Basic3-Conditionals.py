# 程序结构
# if 条件, if后面记得：
a = 100
if a >= 5:
    a -= 5
    print(a)

# while
b = 100
while b >= 5:
    b -= 5
    print(b)

# Exercise：判断奇偶
number = int(input("Enter a integer"))  # 注意要把他转为int型，要不然默认str
if number % 2 == 0:
    print('Even')
else:
    print('Odd')

# 注意else if 在python里是elif
if b == 5:
    b -= 1
elif b == 6:
    b -= 2
else:
    b -= 3

    # python里类似三元表达式的表达

    q = int(input('First Number'))
    w = int(input('Second Number'))
if q == w:
    print('Equal')
else:
    print('q is larger ' if q >= w else 'w is larger')  # 之前的是满足的条件，之后的是不满足的条件

# pass的用法，用在代码没想好的时候,不执行该条件
e = int(input('Enter'))
if e <= 5:
    pass
else:
    print('Too big')

# range函数属于内置函数，默认步长为1,注意range函数是左闭右开——>[...)
# 1.range(stop) with only one parameter,默认从0开始
R = range(10)
print(R)  # range(0, 10)
print(list(R))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 2. range(start, stop) with two parameters, 左闭右开 [)
K = range(2, 8)
print(K)  # range(2, 8)
print(list(K))  # [2, 3, 4, 5, 6, 7]

# 3. range(start, stop, step) with three parameters, 第三个para代表的是是步长，所以步长不再是默认的1
T = range(1, 10, 2)
print(T)  # range(1, 10, 2)
print(list(T))  # [1, 3, 5, 7, 9]

# 可以用in 和not in 判断是否存在
print(9 in T)  # True
print(6 not in K)  # False

# Find the length of the range List
print(len(T))
