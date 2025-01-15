import sympy
from sympy import oo, pi, I

'''
定义函数
'''
x = sympy.Symbol('x')
f = sympy.Function('f')(x)  # 声明函数，x是自变量,括号里的（'f'）只是函数名 后面的括号里是自变量的声明，如果是多元微积分，则可以放(x,y,z,...)
print(sympy.diff(f, x))  # Derivative(f(x), x)

# 求二次导
print(sympy.diff(f, x, x))

# 三次导
print(sympy.diff(f, x, 3))

# multivariable
y = sympy.Symbol('y')
g = sympy.Function('g')(x, y)
print(sympy.diff(g, x, y))

# 求导
expr = x ** 4 + x ** 3 + 2 * x ** 2 + 4
print(sympy.diff(expr))  # 4*x**3 + 3*x**2 + 4*x 一次
print(sympy.diff(expr, x, x))  # 2*(6*x**2 + 3*x + 2) 二次
print(sympy.diff(expr, x, 3))  # 6*(4*x + 1) 三次

'''
Integrals
'''
a, b, x, y = sympy.symbols("a,b,x,y")  # 一次性声明多个symbols
f = sympy.Function('f')(x)
print(sympy.integrate(f))  # Integral(f(x), x)
print(sympy.integrate(f, (x, a, b)))  # 这个的意思是函数f对x求积分，a为lower limit， b 为upper limit

print(sympy.integrate(sympy.sin(x), x))  # -cos(x)
print(sympy.integrate(sympy.sin(x), (x, 1, 0)))  # -1 + cos(1)
print(sympy.integrate(sympy.sin(x), (x, 2 * pi, pi / 2)))  # 1

expr = x ** 2 + y ** 2
print(sympy.integrate(expr, y))  # 对y求偏积分
expr = sympy.integrate(expr, y)
print(sympy.diff(expr, y))  # x**2 + y**2 对y求偏导
# 同时对两个求积分
x, y = sympy.symbols("x,y")
expr = (x + y) ** 2
print(sympy.integrate(expr, x, y))

'''
Series级数
'''
'''
limits
'''
f = sympy.Function('f')(x)
print(sympy.limit(sympy.sin(x) / x, x, 0))  # 1 最后一个参数0指逼近0的时候
expr = (x ** 2 - 3 * x) / (x * 2 - 2)
print(sympy.limit(expr / x, x, sympy.oo))  # 1/2

'''
sum and products
'''

# 求和
n = sympy.Symbol('n', integer=True)
x = sympy.Sum((1 / (n ** 2)), (n, 1, oo))  # n从1开始一直到正无穷 求和
print(x.doit())  # pi**2/6

# 求积
x = sympy.Product(n, (n, 1, 7))  # 1x2x3x4x5x6x7
print(x.doit())  # 5040


'''
equations
'''
x = sympy.Symbol('x')
print(sympy.solve(x**2+2*x-3,x)) # [-3, 1]
print(sympy.solve(sympy.sin(x) - sympy.cos(x),x)) #[pi/4]

'''方程组'''
eq1 = x+2*y-1
eq2 = x-y+1
print(sympy.solve([eq1,eq2],[x,y])) # {x: -1/3, y: 2/3}



