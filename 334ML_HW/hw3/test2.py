import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

df = pd.read_csv('/Users/apple/Desktop/2023FALL/cs334-hw3_template/energydata/eng_xTrain.csv')

date = df['date']
date = pd.to_datetime(date, format='%m/%d/%y %H:%M')
year = date.dt.year.astype(int)
month = date.dt.month
day = date.dt.day
hour = date.dt.hour
minute = date.dt.minute

# time = hour.astype(str) + ':' + minute.astype(str).str.zfill(2)

df.insert(0, 'minute', minute)
df.insert(1, 'Month', month)
df.insert(2, 'Day', day)
df.insert(3, 'hour', hour)
# year/month/day/time/date
df = df.drop(columns=['date'])
# year/month/day/time/
print(df)

corrMat = df.corr()

print(corrMat)

df = pd.read_csv('/Users/apple/Desktop/2023FALL/cs334-hw3_template/energydata/eng_xTrain.csv')
print(df)
df = df.drop(columns=['date'])
print(df)

beta = np.array([1.0, 2.0, 3.0])  # 1D array with shape (3,)

xi = np.array([[1.0, 2.0, 3.0],
               [4.0, 5.0, 6.0],
               [7.0, 8.0, 9.0]])  # 2D array with shape (3, 3)

yi = np.array([[10.0],
               [20.0],
               [30.0]])  # 2D array with shape (3, 1)


def grad_pt(beta, xi, yi):
    """
    Calculate the gradient for a mini-batch sample.

    Parameters
    ----------
    beta : 1d array with shape d
    xi : 2d numpy array with shape b x d
        Batch training data
    yi: 2d array with shape bx1
        Array of responses associated with training data.

    Returns
    -------
        grad : 1d array with shape d
    """
    # 如果你的模型具有N个参数（特征），那么梯度将有N个元素
    # 第一列加上1 要加吗？？？？？
    # ones = np.ones(xi.shape[0])
    # xi_sub = xi
    # xi_sub = np.hstack((ones, xi_sub))  # xi_sub是加了1的可以与beta点乘

    num_sample = xi.shape[0]
    num_feat = xi.shape[1]

    y_actual = yi.reshape(-1, 1)
    y_predict = np.dot(xi, beta).reshape(-1, 1)  # xi要加一列1在最前面吧。。。
    residual = y_actual - y_predict
    print('yi', yi)
    print('y_actual', y_actual)
    print('y_predict', y_predict)
    print('residual:', residual)

    # gradient = xT(residual)/n
    gradient = np.dot(xi.T, residual) / num_sample  # use xi or xi_sub? with or without 1 col?
    return gradient.flatten()


print(grad_pt(beta, xi, yi).shape)
print(grad_pt(beta, xi, yi))

# beta = np.arange(5)
# gradient = np.arange(5).reshape(-1, 1)
#
# result = (beta - gradient)
#
# print(result.shape)
# print(result)
#
# print(beta)
# print(gradient)

xTrain = pd.read_csv('/Users/apple/Desktop/2023FALL/cs334-hw3_template/energydata/eng_xTrain.csv')
yTrain = pd.read_csv('/Users/apple/Desktop/2023FALL/cs334-hw3_template/energydata/eng_yTrain.csv')
xTest = pd.read_csv('/Users/apple/Desktop/2023FALL/cs334-hw3_template/energydata/eng_xTest.csv')
yTest = pd.read_csv('/Users/apple/Desktop/2023FALL/cs334-hw3_template/energydata/eng_yTest.csv')


def cal_corr(df, figsize=(8, 8), annot_fontsize=2):
    """
    Given a pandas dataframe (include the target variable at the last column),
    calculate the correlation matrix (compute pairwise correlation of columns)

    Parameters
    ----------
    df : pandas dataframe
        Training or test data (with the target variable)
    figsize : tuple, optional
        Figure size for the heatmap (width, height)
    annot_fontsize : int, optional
        Font size for annotation text

    Returns
    -------
    corrMat : pandas dataframe
        Correlation matrix
    """
    # Calculate the correlation matrix
    corrMat = df.corr()

    # Create a larger heatmap with larger annotation font size
    plt.figure(figsize=figsize)
    sns.heatmap(corrMat, annot=True, cmap='coolwarm', fmt=".2f", annot_kws={"size": annot_fontsize}, cbar_kws={"shrink": 0.7})

    plt.title('Correlation Matrix Heatmap')  # Add a title to the heatmap
    plt.show()

    return corrMat


xTrain = xTrain.drop(columns=['date'])
xTrain = pd.concat([xTrain, yTrain], axis=1)
cal_corr(xTrain, figsize=(7,7), annot_fontsize=5)
xTrain1= pd.read_csv('/Users/apple/Desktop/2023FALL/cs334-hw3_template/energydata/eng_xTrain.csv')
xTrain2 = xTrain1.drop(columns = ['T1'])
xTrain2.to_csv('/Users/apple/Desktop/2023FALL/cs334-hw1_template/new_csv', index=False)

