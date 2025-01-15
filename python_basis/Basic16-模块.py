# 模块 module

import math

print(id(math))
print(type(math))
print(math)
print(math.pow(2, 3), type(math.pow(2, 3)))
print(math.ceil(7.3))
print(math.floor(7.3))

# 如果不想用math.
from math import pow

print(pow(2, 4))

import Calc

print(Calc.add(3, 4))

import Calc2

print(Calc2.add(1, 2))  # 这段代码，会执行Calc2中另一个部分的内容，即打印heihei what if 我们不需要他？

# 我们可以让function call只执行calc2中的主函数，使用main关键字
if __name__ == '__main__':
    print(Calc2.add(8, 2))  # print heihei不会被执行，因为它不属于主函数

import Calc2 as c  # 这是给calc2取个小名，便于更简单的使用

if __name__ == '__main__':
    print(c.add(1, 4))

    # 导入别的包里的模块就是 import package.module as xxx // from package import module

    # 也可以导入某个包里某个模块里的某个函数 from package.module import FUNCTION NAME

