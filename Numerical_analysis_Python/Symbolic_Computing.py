import sympy  # 这个更偏向于symbol
from sympy import I, pi, oo

'''
create an symbol
'''
x = sympy.Symbol("x")
print(x)

# 定义实数
x = sympy.Symbol("x", real=True)
print(x.is_real)  # true

# 虚数 imaginary
x = sympy.Symbol("x", imaginary=True)
print(x.is_real)  # false

# 根号
x = sympy.Symbol("x", real=True, positive=True)
print(sympy.sqrt((x ** 2)))  # x

# Trigonometry
x = sympy.Symbol("x")
print(sympy.cos(x * pi))  # cos(pi*x)
x = sympy.Symbol("x", integer=True)
print(sympy.cos(x * pi))  # (-1)**x
x = sympy.Symbol("x", odd=True)
print(sympy.cos(x * pi))  # -1

'''
numbers
'''

b = sympy.Integer(77)
print(type(b))
print(b.is_real, b.is_integer, b.is_Boolean)  # TTF

b = sympy.Float(7.8)
# 重复之前的操作即可

print(b ** 2)  # 60.8400000000000

# sympy自带的阶乘算法
print(sympy.factorial(4))  # 24

'''
分数
'''
b = sympy.Rational(1, 2)
c = sympy.Rational(3, 4)
print(b)  # 1/2
print(b * c)  # 3/8

''' 
constants
'''
print(sympy.pi)
print(sympy.E)  # natural log
print(sympy.EulerGamma)  # 欧拉常数
print(sympy.oo)  # infinity
print(sympy.sin(pi * 1.5))  # -1

'''
functions
'''
print(sympy.sin(pi * 1.5))  # -1
d = sympy.Symbol("d", Integer=True)
print((sympy.sin(pi * d)))

# lambda函数
d = sympy.Lambda(x, x ** 3)
print(d(4))  # 64

d = sympy.Lambda(x, 3 * (x + 3))
print(d(3))  # 18

'''
expression
'''
x = sympy.Symbol("x")
expr = x ** 2 + x + 1
print(expr)

# 对于expression的分解，分解为类似array的东西
print(expr.args)  # 注意是反着来的 (1, x, x**2)
print(expr.args[1])  # x
print(expr.args[2].args[1])  # 2

# 自动化简
expr = 2 * x ** 2 - 2 * x
print(sympy.simplify(expr))  # 2*x*(x - 1)
expr = 2 * sympy.cos(x) * sympy.sin(x)
print(sympy.simplify(expr))  # sin(2*x)

# 展开
expr = 2 * (2 * x ** 2 + 1)
print(sympy.expand(expr))  # 4*x**2 + 2

print(sympy.sin(2 * x).expand(trig=True))  # 2*sin(x)*cos(x) trig = true意味着你指示使用三角函数展开

expr1 = x ** 2 + x
expr2 = x * (x + 1)
print(sympy.simplify(expr1) == sympy.simplify(expr2))  # 必须要化简后才能相等，不化简可能会返回false

# factor
expr = (x + 1) * (x + 1) * (x - 1)
print(sympy.expand(expr))  # x**3 + x**2 - x - 1
print(sympy.factor(x ** 3 + x ** 2 - x - 1))  # (x - 1)*(x + 1)**2

# partially-factor 比如x+y+x*y*z不能被fully factor但是可以被collect来partialy factor
y = sympy.Symbol("y")
z = sympy.Symbol("z")
expr = x + y + x * y * z
print(expr.collect(x))  # x*(y*z + 1) + y
print(expr.collect(y))  # x + y*(x*z + 1)

# 分数的操作
print(sympy.together((1 / x ** 2) + (2 / x ** 2)))  # 3/x**2 分数合
print(sympy.apart(1 / (x ** 2 + 3 * x + 2), x))  # -1/(x + 2) + 1/(x + 1) 指定对x进行factorization
print(sympy.cancel((x - 1) / (x ** 2 - x)))  # 1/x

# substitution sub(x,y)x被y替代
print((x * sympy.exp(x ** 2)).subs(x, z))  # z*exp(z**2)

