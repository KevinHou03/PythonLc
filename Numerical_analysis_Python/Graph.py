import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

# First, instance Figure creates a canvas area for drawing
'''
1.创建所有参数，比如x range
2.创建画板，比如Figure，Axes instance
3.Set graph properties比如label
4.Generate Legend
'''

# 画 x^3 + 5x^2 + 10
'''
# 1.set 参数
x = np.linspace(-5, 2, 100)
y_1 = x ** 3 + 5 * x ** 2 + 10
y_2 = 3 * x ** 2 + 10 * x
y_3 = 6 * x + 10

fig, ax = plt.subplots()  # 这代表一幅图，如果你要三幅图for三个函数，你要写三个这个 fig1/2/3, ax1/2/3
ax.plot(x, y_1, color="blue", label="y(x)")
ax.plot(x, y_2, color="red", label="y'(x)")
ax.plot(x, y_3, color="green", label="y''(x)")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.legend()
plt.show()
'''

# 画一个cos和sin
x = np.linspace(-4 * np.pi, 4 * np.pi, 100)
print(type(x))
y_3 = np.cos(x)
print(type(y_3))
y_4 = np.sin(x)

fig2, ax2 = plt.subplots()
ax2.plot(x, y_3, color="black")
ax2.plot(x, y_4, color="blue")
ax2.axhline(y=0, color="red", linestyle="-", label="x-axis")  # Adding x-axis line
ax2.set_xlabel("x")
ax2.set_xlabel("y")
ax2.legend()
#plt.show()

a = [1,2,3,4,5]
print(type(a))
a_array = np.array(a)
print(type(a_array))


'''
A Figure object can be created using the function plt.figure, which takes several optional keyword arguments for 
setting figure properties. In particular, it accepts the figsize keyword argument, which should be assigned to a 
tuple on the form (width, height), specifying the width and height of the figure canvas in inches. It can also be 
useful to specify the color of the figure canvas by setting the facecolor keyword argument.

Once a Figure is created, we can use the add_axes method to create a new Axes instance and assign
it to a region on the figure canvas. The add_axes takes one mandatory argument: a list containing the coordinates of 
the lower-left corner and the width and height of the Axes in the figure canvas coordinate system, 
on the format (left, bottom, width, height).
'''

'''
def fwd_solve_row_banded(a, b, k):
    n = np.size(b)
    x = np.zeros(n)
    x[0] = b[0] / a[0, 0]
    count = 0
    for i in range(1, k):  # 1
        x[i] = (b[i] - np.inner(a[i, 0:i], x[0:i])) / a[i, i]
        # count = i

    for i in range(k, a.shape[0]):
        # count2 = i - k
        x[i] = (b[i] - np.inner(a[i, (i - k):i], x[(i - k):i])) / a[i, i]
        # count2 += 1
    return x
def upper_calculation_forward(matrix, vector, band_width):
  has_expected_width_upper(matrix,band_width)
  answer = []
  another_index = 0
  for i in range(0, matrix.shape[0] - band_width): # 012
    vector_index = i # 012 -
    result = 0
    for j in range (0,band_width + 1): # 012
      result += (matrix[i][vector_index] * vector[vector_index])
      vector_index += 1
    answer.append(result)
    another_index += 1
    #print('vector_index after first round', another_index)


  vector_index = another_index # 3 这个在循环外更新
  vector_index2 = another_index # 3 这个在循环内更新
  for i in range(band_width,0,-1): # 2,1
    result = 0
    for j in range(0,i): # 0, 1 # 0
      result += (vector[vector_index + j] * matrix[vector_index][vector_index + j])
      #vector_index2 += 1
    vector_index += 1
    answer.append(result)
    #print("vector index1:",vector_index )
    #print("vector index2:",vector_index2)


  return answer
'''
'''
def upper_calculation_backward(matrix, vector, band_width): # 12333
  has_expected_width_upper(matrix,band_width)
  answer = []
  vector_index = 0
  for i in range(0, band_width): # 01
    result = 0
    for j in range(0,i+1):# 0 # 01
        result += (vector[j] * matrix[j][i])
    vector_index += 1
    answer.append(result)
    # vector_index += 1 : 2
    print('vector_index after first part', vector_index)
  aux = 0
  for i in range(0,matrix.shape[0] - band_width): # 012
    result = 0
    for j in range(0, band_width + 1): # 012
        result += (matrix[i][vector_index] * vector[i])
        i += 1
    answer.append(result)
    vector_index += 1
    aux += 1

  return answer
'''
'''
def lower_calculation_forward(matrix, vector, band_width):
    # Exception handling
    # has_expected_width_lower(matrix, band_width)
 # has_expected_width_lower(matrix,band_width)
    answer = []
    vector_index = 0
    for i in range(0, band_width):
      result = 0
      for j in range(0,i+1):
          result += (matrix[i][j] * vector[vector_index])
      answer.append(result)
      vector_index += 1
      # print('vector_index after first part', vector_index)

    aux = 0
    for i in range(band_width,matrix.shape[0]): # 234
      result = 0
      for j in range(0, band_width + 1): # 012
          result += (matrix[i][j+aux] * vector[vector_index])
      answer.append(result)
      vector_index += 1
      aux += 1
    return answer
'''

'''
def lower_calculation_back(matrix, vector, band_width):
  # Exception handling
  has_expected_width_lower(matrix,band_width)
  answer = []
  another_index = 0
  for i in range(0, matrix.shape[0] - band_width): # 012
    vector_index = i # 012 -
    result = 0
    for j in range (0,band_width + 1): # 012
      result += (vector[vector_index] * matrix[vector_index][i])
      vector_index += 1
    answer.append(result)
    another_index += 1
    # print('vector_index after first round', another_index)

  vector_index = another_index # 3 这个在循环外更新
  vector_index2 = another_index # 3 这个在循环内更新
  for i in range(band_width,0,-1): # 2,1
    result = 0
    for j in range(0,i): # 0, 1 # 0
      result += (vector[vector_index + j  ] * matrix[vector_index + j][vector_index])
      #vector_index2 += 1
    vector_index += 1
    answer.append(result)
    # print("vector index1:",vector_index )
    # print("vector index2:",vector_index2)

  return answer
'''