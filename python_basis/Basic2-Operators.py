from decimal import Decimal

# 输入函数 input() 执行该程序，然后你自己输入答案，之后按照print函数把你的答案输出出来
Answer = input('What do you want？')  # type str
print(Answer)

# Exercise：键盘输入两个数，输出两个数的和
TheFirstNumber = input("Type the first number")
TheSecondNumber = input("Type the second number")
Answer = int(TheFirstNumber) + int(TheSecondNumber)  # input 函数默认的事str，所以要转化为int
print(Answer)

# 运算符号中 无非是 +—*/， 但是python有特殊的 包括整除// 和 幂**，然后python不会round down/up,就会直接输出小数
print(99 // 5)  # 取到整数部分19
print(2 ** 7)  # 2的七次方

# 在一正一负的情况下，有一些需要注意,因为一正一负，向下取整
print(-9 // -4)  # 2
print(9 // 4)  # 2
print(9 // -4)  # -3 向下取整
print(-9 / 4)  # -3 向下取整

# 在一正一负时，对于余数 remainder=被除数-除数*商
print(9 % -4)  # -3
print(-9 % 4)  # 3

# 赋值运算符，从右往左 1.支持链式赋值,而且链式里面的元素的地址值会是一样的 2.支持参数赋值
a = b = c = 20  # 链式
a += 20  # 参数赋值
i, j, k = 10, 20, 30  # 解包赋值

# python中的代码交换，十分简洁
e, d = 22, 45
e, d = d, e  # 交换完毕

# 比较运算符，与java相同 = 是赋值运算符，==是比较运算符，主要比较value    is主要比较地址值,一定要注意
p = 10
q = 10
print(p == q)  # true value is the same
print(p is q)  # true address is the same
print(p is not q)  # false, 他们地址是一样的
list1 = [1, 2, 3, 4]
list2 = [1, 2, 3, 4]
print(list1 == list2)  # true
print(list1 is list2)  # false, different address]

# &&在python里直接用 and ｜｜直接用or 如果要negating一个statement 直接用not 取反
s = True
f = False
print(s == 1 or f == 0)
print(s == 0 and f == 1)
print(not f)

# in and not in 判断元素包含关系
u = "HelloWorld"
print('o' in u)

# 位运算符 换算为二进制运算， 补齐8位
print(4 & 8)  # 答案为0 同为'与' 对应位置都为1则为1，其余为0
print(4 | 8)  # 答案为12 同为'或' 有一个1则1，没有1则0
