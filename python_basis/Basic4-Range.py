# 循环
# If statement will only execute once
import numpy as np

a = 1
if a < 10:
    print(a)
    a += 1

# while statement will execute until the condition fails
b = 1
while b <= 10:
    print(b)
    b += 1

# Exercise:计算0-4的整数累加和
c = 0
Sum = 0
while c <= 4:
    Sum += c
    c += 1
print(Sum)

# Exercise: 计算1-100的偶数和
d = 0
Sum2 = 0
while d <= 100:
    if d % 2 == 0:
        Sum2 += d
    d += 1
print(Sum2)

# Another method
e = 0
Sum3 = 0
while e <= 100:
    Sum3 += e
    e += 2
print(Sum3)

# for-in 循环 遍历
for item in 'KaiYuanHou':
    print(item)

A = range(1, 11, 2)
for item2 in A:
    print(item2)  # 1,3,5,7,9

# 甚至可以不定义变量，直接用下划线_代替
for _ in range(1, 8):
    print("Love")  # Love x 7

    # 用for计算1-100偶数和
    f = 0
    Sum4 = 0
    for item in range(0, 101):
        if item % 2 == 0:
            Sum4 += item
    print(Sum4)

# Exercise: between 100-999, find all numbers such that ABC=A^3+B^3+C^3
for item in range(100, 1000):
    s = str(item)
    unit = int(s[0])
    tens = int(s[1])
    hundred = int(s[2])
    result = unit ** 3 + tens ** 3 + hundred ** 3
    if result == item:
        print(item)

# how to use break: quit the loop
for item in range(3):  # you have three chances for your password
    password = input("enter your password")
    if password == '0527':
        print('Correct')
        break  # once the password is correct, quit, no matter how many chances you have left
    else:
        print('Incorrect')

# how to use continue: 结束当前循环，而不是像break一样结束一切循环
# Exercise: 找出1-50所有5的倍数
# Method1：
for item in range(1, 51):
    if item % 5 == 0:
        print(item)
# Method2: use continue
for item in range(1, 51):
    if item % 5 != 0:
        continue  # skip all those that can be divided by 5
    print(item)

# else语句
for item in range(3):  # you have three chances for your password
    password = input("enter your password")
    if password == '0527':
        print('Correct')
        break  # once the password is correct, quit, no matter how many chances you have left
    else:
        print('Incorrect')
else:  # watch for the parallel relationship, this happens when all chances are used up
    print("No chances left")

    # while else
    a = 0
    while a < 3:
        password = input("enter your password")
        if password == '0527':
            print('Correct')
            break  # once the password is correct, quit, no matter how many chances you have left
        else:
            print('Incorrect')
        a += 1
    else:
        print("No chances left")

# 嵌套循环 Exercise：打印五角星金字塔
for i in range(1, 10):
    for j in range(1, i):
        print('*', end='')
    print('')

    # 循环嵌套中的break和continue
for i in range(5):
    for j in range(1, 11):
        if j % 2 == 0:
            break
        print(j)  # 11111

for i in range(5):
    for j in range(1, 11):
        if j % 2 == 0:
            continue
        print(j, end='\t')
    print('')

a = np.array([1, 2, 3, 4])
a = a ** 2
print(a)

