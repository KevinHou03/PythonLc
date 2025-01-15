"""
函数Def，就是java里的method

def 函数名（parameters）
函数体
return xxx
"""
"""
对于不可变变量，int str等，函数不会改变变量本身。
"""


def CalcSum(a, b):
    c = a + b
    return c


print(CalcSum(3, 5))  # 8
print(CalcSum(b=5, a=3))  # 反过来也可行，但是要声明变量名了


def OddEvenList(num):
    odd = []
    even = []
    for items in num:
        if items % 2 == 0:
            even.append(items)
        else:
            odd.append(items)
    return odd, even


'''
注意同时返回两个值，都为列表
'''

print(OddEvenList([1, 2, 3, 4, 5, 6, 7, 8, 9]))  # ([1, 3, 5, 7, 9], [2, 4, 6, 8])

"""
1.个数可变位置参数，有时我们不确定一个方法需要几个位置实数，定义时可用*定义个数可变的形参，结果为一个元祖
2.无法确定传递的关键字实参个数，用可变的关键字形参**,结果为一个字典
3.可变的位置参数，只能写一个。
4.可变的关键字参数，也只能写一个。
5.可以定义一个位置参数，一个关键字参数
"""


def function(*parameters):
    print(parameters)


function(10)  # (10,)
function(10, 20)  # (10, 20)
function(10, 20, 30)  # (10, 20, 30)


def function2(**parameters):
    print(parameters)


function2(a=10)  # {'a': 10}
function2(a=20, b=38, c=83)  # {'a': 20, 'b': 38, 'c': 83}


def function3(*para1, **para2):
    print(para1, para2)


function3(3, a=9)  # (3,) {'a': 9}

"""
对于位置形参而言：
"""


def function3(para1, para2, para3):
    print(para1)
    print(para2)
    print(para3)


function3(10, 20, 30)  # 10,20,30，这里自动按照p1=10 p2=20 p3=30,位置对应关系，所以这就叫位置形参

# 如果我用一个list传进去呢？
list = [10, 20, 30]
# function3(list)  报错
function3(*list)

"""
将局部变量变为全局变量
"""


def fun4(a, b):
    c = a + b
    global d  # d现在是一个全局变量
    d = 'name'
    e = 'age'  # e是一个局部变量
    print(d)


fun4(1, 2)
print(d)  # 全局变量在func外部也可以调用，但是局部变量就不可以。

"""
递归，在方法里调用方法本身
"""


def Factorial(a):
    if a == 1:
        return a
    else:
        return a * Factorial(a - 1)


print(Factorial(5))


def Fibonacci(a):  # return the ath fibonacci number.
    if a == 1:
        return 0
    if a == 2:
        return 1
    else:
        return Fibonacci(a - 1) + Fibonacci(a - 2)


print(Fibonacci(12))


def FibonacciAdvanced(a):  # generate a Fibonacci sequence with a elements.
    Result = []
    for element in range(1, a + 1):  # 注意左闭右开
        temp = Fibonacci(element)
        Result.append(temp)
    return Result


print(FibonacciAdvanced(9))
