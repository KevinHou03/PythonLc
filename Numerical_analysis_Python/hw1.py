import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np


def draw_three_functions():
    fig1 = plt.figure()
    fig2 = plt.figure()
    fig3 = plt.figure()

    ax1 = fig1.add_subplot(projection='3d')
    ax2 = fig2.add_subplot(projection='3d')
    ax3 = fig3.add_subplot(projection='3d')

    x1 = np.linspace(-3, 3, 1000)
    y1 = np.linspace(-3, 3, 1000)

    x2 = np.linspace(-2, 2, 1000)
    y2 = np.linspace(-4, 4, 1000)

    x3 = np.linspace(-2, 2, 1000)
    y3 = np.linspace(-1, 1, 1000)

    X1, Y1 = np.meshgrid(x1, y1)
    X2, Y2 = np.meshgrid(x2, y2)
    X3, Y3 = np.meshgrid(x3, y3)

    Z1 = (X1 ** 2 + 3 * Y1 ** 2) * np.exp(-X1 ** 2 - Y1 ** 2)
    Z2 = (-3 * Y2) / (X2 ** 2 + Y2 ** 2 + 1)
    Z3 = np.abs(X3) + np.abs(Y3)

    plot1 = ax1.plot_surface(X1, Y1, Z1, color='red')
    plot2 = ax2.plot_surface(X2, Y2, Z2, color='blue')
    plot3 = ax3.plot_surface(X3, Y3, Z3, color='green')

    # Set axis labels and title
    ax1.set_xlabel('X')
    ax1.set_ylabel('Y')
    ax1.set_zlabel('Z')
    ax1.set_title('(x^2+3y^2)e^(-x^2-y^2)')

    ax2.set_xlabel('X')
    ax2.set_ylabel('Y')
    ax2.set_zlabel('Z')
    ax2.set_title('-3y/(x^2+y^2+1)')

    ax3.set_xlabel('X')
    ax3.set_ylabel('Y')
    ax3.set_zlabel('Z')
    ax3.set_title('|x|+|y|')

    # Show the plot
    # plt.show()


def compute_formula_derivative(x, h):
    return (np.cos(x) - np.cos(x - h)) / h


def compute_real_derivative(x):
    return -np.sin(x)


def compute_error(x, h):
    return abs(compute_formula_derivative(x, h) - compute_real_derivative(x))


def compute_all_errors():
    ANSWER_SET = []
    K_VALUE = range(1, 13)
    H_VALUE = [10 ** (-k) for k in K_VALUE]
    for i in H_VALUE:
        error = compute_error(1.5, i)
        ANSWER_SET.append(error)
    return ANSWER_SET


'''
print(compute_all_errors())
print(compute_error(1.5,10**(-1)))
print(compute_error(1.5,10**(-2)))
print(compute_error(1.5,10**(-3)))
print(compute_error(1.5,10**(-4)))
print(compute_error(1.5,10**(-5)))
print(compute_error(1.5,10**(-6)))
'''


def draw_error():
    fig, ax = plt.subplots()
    k_value = range(1, 13)  # 1-12
    x = [10 ** (-k) for k in k_value]
    x_array = np.array(x)
    x_axis = np.linspace(1, 12, 12)
    # print(x_axis)
    # print(x_array)
    y = compute_error(1.5, x_array)
    # print(y)
    ax.plot(x_axis, y)
    ax.set_xlabel('K value')
    ax.set_ylabel('Error')
    ax.set_title('Error_k_graph')
    plt.show()


draw_three_functions()
draw_error()
print(compute_all_errors())

'''
Reasoning:
The nature of derivative, especially first-order is moving a trivial step 
forward/backward and calculate the value of y-difference and the length of 
the 'step', so, as h gets smaller and smaller, the difference between 'x'
and 'x-h' decreases, thus the calculation becomes more and more accurate. 
This is caused by convergence, as h->0, the approximation gets closer to the
true derivative.

Also, as h gets significantly small, the error caused by floating point 
arithmetics could be manifested, as we can see that the line goes down initially
, but after a certain point, where h gets too small and exceeds the digit-limit 
of python interpreter, the precision lost caused by floating point arithmetic
could be shown in the graph, as the line goes up a bit when k > 11 and approaching
12.
'''
