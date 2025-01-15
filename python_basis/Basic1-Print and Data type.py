print('HelloWorld')
# 对于print的解释：
print(520)  # number
print('I love You')  # String, you have to use''or""
print("I Love You")
print(2 + 1)  # expression, the output will be 3, the result, not the expression

# 将数据输出到文件中
# address = open()
# print("love", file=address)
# address.close()

# 如何把几个元素打印在同一行？用逗号隔开
print('Hi', 250, 3 * 9)

# 转义字符，反斜杠+关键字首字母
print('hello\nworld')  # 两个之间就会换行 Newline
print('hello\tworld')  # 加空格
print('hello\rworld')  # return回车，只会输出world
print('hello\bworld')  # 退一个格--hellworld

# 在string里面加单引号输出，用反斜线
print('He said:\'You are right\'')

# 原字符：使转义字符失效：在字符串前加r或R
print(r'hello\nworld')  # 注意：使用的时候字符串最后一个字不能是反斜杠\, 但是你可以是两个\

# 变量赋值
name = 'Kevin Hou'
age = 19
print(name)

# 变量信息，我们可以通过以下几种方法打印出或者找到变量的具体信息，比如变量类型，变量地址，变量值
print('地址值', id(name))
print('类型', type(name))
print('值', name, age)
# 多次给变量赋值，变量等于最新的赋值
# 常用的python数据类型 int float bool str

# 如何避免float的运算错误？import 小数包
from decimal import Decimal  # 这个应该放在 the top of file

print(Decimal(1.1) + Decimal(2.2))

# boolean
b1 = True  # True=1
b2 = False  # False=0

# 与java不同的是，python中str和其他基本类型不能同时print，必须cast
a = 'hello'
b = 711
c = True
d = '527'
print(a, str(b), str(c))  # 注意cast的语法，括号与java是反着的,这里全部转换为str类型了
print(a, int(d), int(c))  # 也可以把除了str的各类型转为int型，注意str是不能转int的

# float型的转化
print(float(b))  # 711.0
print(float(d))  # 527.0 所以说除了str 其他都可以转float和int型 
print(float(c))
