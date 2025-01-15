import numpy as np

'''
numpy array object
'''
data = np.array([[1, 2],
                 [3, 4],
                 [5, 6]])  # a 2-dimensional NumPy array with three rows and two columns
print(type(data))  # <class 'numpy.ndarray'>
print(data.shape)
print(data.size)  # how many elements: 6
print(data.ndim)  # number of dimensions : 2
print(data.nbytes)  # 一个int  8字节，6个一共：48
print(data.dtype)  # datatype: int

'''
datatype:
int-integer
uint-unsigned int(non-negative)
bool-boolean
float
complex
'''

data2 = np.array([1, 2, 3])
print(data2.dtype)  # int
data3 = np.array([2.0, 3.0])
print(data3.dtype)  # float

# Typecasting,把一个类型的数组强转为另一个类型
data2 = np.array(data2, dtype=np.float64)
print(data2.dtype)  # int -> float

# 也可以用astype，括号里直接写要转成的类型
data3 = data3.astype(np.int64)
print(data3.dtype)  # float -> int

'''
计算每个元素的square root
注意一定要是有root的数，要不报警
'''
data4 = ([16, 25, 36])
data4 = np.sqrt(data4)
print(data4)  # [4. 5. 6.]

'''
Array filled with constants:
'''
# arrays filled with constants
data5 = np.zeros(4, int)  # four elements, and int as datatype
print(data5)  # [0 0 0 0]

data6 = np.zeros((2, 3), float)
print(data6)  # [[0. 0. 0.][0. 0. 0.]] a 2x3 matrix with 0s

data7 = np.ones(4, int)  # filled with 1s
print(data7)  # [1 1 1 1]

# 创造一个全是5.4的3✍x3矩阵,the first method:
data8 = 5.4 * np.ones((3, 3), int)
print(data8)

# the second method: using no.full(elementNumbers, value)
data9 = np.full((3, 3), 5.4)
print(data9)  # the same effect as data8

# create a diagonal matrix, put the value of the diagonal in the array.[]
data10 = np.diag([1, 2, 2])
print(data10)
'''
[[1 0 0]
 [0 2 0]
 [0 0 2]]
'''

# np.Arange: creates an array with evenly spaced values between specified start, end, and increment values
data11 = np.arange(1, 10, 2)
print(data11)  # [1 3 5 7 9]

'''
Array filled with incremental sequence [1,2,3,4,5,6...]
'''
# np.Arange: creates an array with evenly spaced values between specified start, end, and NOT increment values BUT
# element numbers
data12 = np.linspace(1, 10, 3)
print(data12)  # [ 1.0,5.5,10.0 ]

# 如果要[1,2,3,4...10]
data13 = np.linspace(1, 10, 10, dtype=int)
print(data13)  # [ 1  2  3  4  5  6  7  8  9 10]

# logspace
data14 = np.logspace(1, 10, 3)  # 创建一组在对数刻度上均匀分布的数字的函数
print(data14)

# Mesh-Grid:如果有一个function Z = (x+y)^2, 我们有x = [1,2,3] y = [4,5,6],用meshGrid把x和y合并在一起求Z的所有值
x = ([1, 2, 3])
y = ([4, 5, 6])
xM, yM = np.meshgrid(x, y)  # combined
print(xM)  # [[1 2 3][1 2 3][1 2 3]] 理解： xM中每一行都是x的复制，yM中每一行都是y的复制
print(yM)  # n[[4 4 4][5 5 5][6 6 6]]
Z = (xM + yM) ** 2
print(Z)
'''
[[25 36 49]
 [36 49 64]
 [49 64 81]] 所有可能的组合
'''


def add(a, b):
    return a + b


data15 = np.fromfunction(add, (4, 4))  # put it every possible combination of indices.用坐标代入算得
print(data15)
'''
[[0. 1. 2. 3.]
 [1. 2. 3. 4.]
 [2. 3. 4. 5.]
 [3. 4. 5. 6.]]
 '''

# 随机数 生成的数字在0-1之间
data16 = np.random.rand(2, 3)  # 括号里直接写dimension size
print(data16)
'''
[[0.12666173 0.49722263 0.61315665]
 [0.8812725  0.11663376 0.81443238]]
 '''


# 这里有一个类叫做ones_like / zeros_like / full_like / empty_like通过函数传参来创造一个和xxx_like相似的函数，用参数的大小等等

def Similar(x):
    k = np.ones_like(x)
    return k


print(Similar(data16))
'''
[[1. 1. 1.]
 [1. 1. 1.]]
 '''

# identity matrix
data17 = np.identity(5)
print(data17)
'''
[[1. 0. 0. 0. 0.]
 [0. 1. 0. 0. 0.]
 [0. 0. 1. 0. 0.]
 [0. 0. 0. 1. 0.]
 [0. 0. 0. 0. 1.]]
 '''

'''
indexing and slicing 
'''
data = ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(data[3])  # 4
print(data[-4])  # 从右边数从-1开始，7
print(data[2:5])  # print从2到4，但不包括5，坐闭右开
print(data[:])  # print all or using print(data[0:-1])
print(data[:5])  # 从最左边一直到4，不包括5
print(data[7:])  # 从7开始到所有
print(data[2:6:2])  # 从index 2到5，不包括6，但是increment是2
print(data[::-1])  # 倒着print

# 创建一个匿名函数 name = lambda：xxxx(直接return xxx)
f = lambda x, y: y + 10 * x
data18 = np.fromfunction(f, (6, 6), dtype=int)  # fromFunction用的是index
print(data18)
'''
[[ 0  1  2  3  4  5]
 [10 11 12 13 14 15]
 [20 21 22 23 24 25]
 [30 31 32 33 34 35]
 [40 41 42 43 44 45]
 [50 51 52 53 54 55]]
 '''

print(data18[1, :])  # [10 11 12 13 14 15] second row#
print(data18[:, 1])  # [ 1 11 21 31 41 51] second column
# 在使用索引访问多维数组时，放在逗号前面的索引表示行，放在逗号后面的索引表示列,冒号左右表示界
#
print(data18[1, 2:4])  # [12 13]

# 左上小方块
print(data18[0:3, 0:3])  # 行0-3 列0-3
# 右上
print(data18[:3, 3:])

'''
reshape 在总元素不变的情况下，改变矩阵心态
'''
data19 = ([[1, 2], [3, 4], [5, 6]])
data19 = np.reshape(data19, (1, 6))
print(data19)  # [[1 2 3 4 5 6]]
data19 = np.reshape(data19, (3, 2))
print(data19)
'''[[1 2]
    [3 4]
    [5 6]]
'''

'''
flatten 不管你是什么样，都给你降级到一维数组
'''
data19 = data19.flatten()
print(data19)  # [1 2 3 4 5 6]

'''
vstack ，np.vstack 函数用于将数组在垂直方向上堆叠（连接），从而在行方向上组合它们，创建一个具有更多行的新数组 横的变竖的
'''
data20 = ([1, 2, 3, 4])
data20 = np.vstack(data20)
print(data20)
'''
[[1]
 [2]
 [3]
 [4]]
 '''

'''
hstack 与之相对，在水平方向上重叠 例子中，三个data20被水平方向叠放在一起
'''
print(np.hstack((data20, data20, data20)))
'''
[[1 1 1]
 [2 2 2]
 [3 3 3]
 [4 4 4]]
 '''

'''
Arithmetic operations
'''

x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 6], [7, 8]])
print(x + y)
print(y - x)
print(x * y)
print(x * 2)
print(x ** 2)
print(2 ** x)
print(y / 2)
x = np.insert(x, 4, [5, 6])  # (这是创造了一个新array，在x的4位置插入[5,6] 注意[a,b]算两个位置
print(x)

'''
functions like sin() cos()...
'''

data21 = np.linspace(-1, 1, 11)
y = np.sin(np.pi * data21)  # data21指的是data21里面的每一个元素
print(np.round(y, decimals=4))
'''
[-0.     -0.5878 -0.9511 -0.9511 -0.5878  0.      0.5878  0.9511  0.9511
  0.5878  0.    ]
'''

'''add'''
x = ([1, 2, 3, 4, 5, 6, 7, 8])
data21 = np.add(np.sin(x) ** 2, np.cos(x) ** 2)  # 也是对x里面的每一个元素进行运算
print(data21)  # [1. 1. 1. 1. 1. 1. 1. 1.]

a = np.array([1, 2, 3])
a = a ** 2
print(a)

test = ([1, 2, 3])
test2 = np.vstack(test)
print(test2)
B = np.dot(test, test2)
print(type(B))
print(type(B[0]))
print(B[0])

data22 = ([1, 2, 3, 4])
data23 = ([2, 3, 4, 5])
data24 = np.add(data22, data23)
print(data24)  # [3,5,7,9]
data25 = np.power(data22, 2)
print(data25)  # [ 1  4  9 16]
data25 = np.remainder(data22, 2)
print(data25)  # [1 0 1 0]
print(np.reciprocal(data22))  # [1 0 0 0]  1/x

# floor and ceil and round
data26 = ([1.28, 3.48, 8.22, 9.99])
print(np.floor(data26))  # [1. 3. 8. 9.]
print(np.ceil(data26))  # [ 2.  4.  9. 10.]
print(np.round(data26, 1))  # [ 1.3  3.5  8.2 10. ]

# mean/std/var/sum/prod/cumsum/cumprod/MinMax/all/any
data27 = ([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(np.mean(data27))  # 所有平均值
print(np.std(data27))  # standard deviation
print(np.var(data27))  # variance
print(np.sum(data27))  # 所有元素和
print(np.prod(data27))  # 积
print(np.cumsum(data27))  # 累计和
print(np.cumprod(data27))  # 累计积
print(np.min(data27), max(data27))  # 最小值和最大值
print(np.argmin(data27), np.argmax(data27))  # 最小最大值的index
print(np.all(data27))  # true if all nonzero
print(np.any(data27))  # true if at least one is nonzero

'''
set,every element has to be unique 
'''
data28 = np.unique([1, 2, 3, 4, 5, 5, 5, 5])  # unique把你输入的array变成一个set：eliminate all replications
data29 = np.unique([1, 2, 3, 9, 9, 9, 7])
print(data28)  # [1 2 3 4 5]
print(data29)  # [1 2 3 7 9]
print(np.union1d(data28, data29))  # [1 2 3 4 5 7 9]并集
print(np.intersect1d(data28, data29))  # [1 2 3]交集
print(np.setdiff1d(data28, data29))  # [4 5] 在data28却不在data29的
print(np.in1d(data28, data29))  # [ True  True  True False  False] data28中的五个元素在29中有没有出现


'''

'''
