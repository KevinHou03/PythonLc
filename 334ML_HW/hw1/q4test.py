import argparse
import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler

file_path1 = '/Users/apple/Desktop/2023FALL/hw1_template/q4xTest.csv'
df_test = pd.read_csv(file_path1)
# print('测试数据：', df_test)

file_path2 = '/Users/apple/Desktop/2023FALL/hw1_template/q4xTrain.csv'
df_train = pd.read_csv(file_path2)
# print('训练数据：', df_train)

file_path3 = '/Users/apple/Desktop/2023FALL/hw1_template/q4yTest.csv'
df_test_label = pd.read_csv(file_path3)
# print('测试组标签：', df_test_label)


file_path4 = '/Users/apple/Desktop/2023FALL/hw1_template/q4yTrain.csv'
df_train_label = pd.read_csv(file_path4)
# print('训练组标签：', df_train_label)

'''
information = (df_train.describe())
column_information = df_train['fixed acidity'].describe().loc['min']
print(type(df_train['fixed acidity'].describe().loc['min']))  # numpy float
print("column_information", column_information)
print("information:", information)
print("最小值：", information.loc['min'])
print("最大值：", information.loc['max'])
print(type(information.loc['max']))
'''

'''
print(df_train.columns)
for column in df_train.columns:
    df_train[column] = df_train[column] - 10
    print(column, df_train[column])

print(type(df_train))
print(df_train.values)
'''


# this takes two nd arrays as parameters
def standard_scale_ndarray(xTrain, xTest):
    """
    Preprocess the training data to have zero mean and unit variance.
    The same transformation should be used on the test data. For example,
    if the mean and std deviation of feature 1 is 2 and 1.5, then each
    value of feature 1 in the test set is standardized using (x-2)/1.5.

    Parameters
    ----------
    xTrain : nd-array with shape n x d
        Training data
    xTest : nd-array with shape m x d
        Test data

    Returns
    -------
    xTrain : nd-array with shape n x d
        Transformed training data with mean 0 and unit variance
    xTest : nd-array with shape m x d
        Transformed test data using same process as training.
    """
    # TODO FILL IN
    train_mean = np.mean(xTrain)
    train_std = np.std(xTrain)
    test_mean = np.mean(xTest)
    test_std = np.std(xTest)
    '''
    for train_element in xTrain:
        train_element = (train_element - train_mean) / train_std
    for test_element in xTest:
        test_element = (test_element - test_mean) / test_std
        '''
    xTrain = (xTrain - train_mean) / train_std
    xTest = (xTest - test_mean) / test_std

    return xTrain, xTest


print("test for standard scale:")
nd1 = np.array([13, 87, 59, 92, 88])
nd2 = np.array([18, 7, 31, 98, 84])

print("before scale, mean:")
print(np.mean(nd1))
print(np.mean(nd2))

print("before scale, std:")
print(np.std(nd1))
print(np.std(nd2))

nd1_scale, nd2_scale = standard_scale_ndarray(nd1, nd2)

print("after scale, mean:")
print(np.mean(nd1_scale))
print(np.mean(nd2_scale))
print("after scale, std:")
print(np.std(nd1_scale))
print(np.std(nd2_scale))


def standard_scale_DataFrame(xTrain, xTest):
    """
    Preprocess the training data to have zero mean and unit variance.
    The same transformation should be used on the test data. For example,
    if the mean and std deviation of feature 1 is 2 and 1.5, then each
    value of feature 1 in the test set is standardized using (x-2)/1.5.

    Parameters
    ----------
    xTrain : nd-array with shape n x d
        Training data
    xTest : nd-array with shape m x d
        Test data

    Returns
    -------
    xTrain : nd-array with shape n x d
        Transformed training data with mean 0 and unit variance
    xTest : nd-array with shape m x d
        Transformed test data using same process as training.
    """
    # TODO FILL IN
    train_mean = xTrain.mean()
    train_std = xTrain.std()
    test_mean = xTest.mean()
    test_std = xTest.std()
    '''
    for train_element in xTrain:
        train_element = (train_element - train_mean) / train_std
    for test_element in xTest:
        test_element = (test_element - test_mean) / test_std
    '''

    xTrain = (xTrain - train_mean) / train_std
    xTest = (xTest - test_mean) / test_std

    return xTrain, xTest


print("对于def standard_scale_DataFrame的测试：")
data1 = {'Feature1': [1, 2, 3, 4, 5],
         'Feature2': [10, 20, 30, 40, 50],
         'Feature3': [100, 200, 300, 400, 500]}
df1 = pd.DataFrame(data1)

data2 = {'Feature1': [1, 2, 3, 4, 5],
         'Feature2': [10, 20, 30, 40, 50],
         'Feature3': [100, 200, 300, 400, 500]}
df2 = pd.DataFrame(data2)

print("scale之前的均值", df1.mean(), df2.mean())
print("scale之前的std", df1.std(), df2.std())

data1M, data2M = standard_scale_DataFrame(df1, df2)
df1M = pd.DataFrame(data1M)
df2M = pd.DataFrame(data2M)

print("scale之后的均值", df1M.mean(), df2M.mean())
print("scale之后的std", df1M.std(), df2M.std())


def minmax_range(xTrain, xTest):
    """
    Preprocess the data to have minimum value of 0 and maximum
    value of 1.The same transformation should be used on the test data.
    For example, if the minimum and maximum of feature 1 is 0.5 and 2, then
    then feature 1 of test data is calculated as:
    (1 / (2 - 0.5)) * x - 0.5 * (1 / (2 - 0.5))
    (1/(max - min)) * x - min * (1/(max-min))

    Parameters
    ----------
    xTrain : nd-array with shape n x d
        Training data
    xTest : nd-array with shape m x d
        Test data

    Returns
    -------
    xTrain : nd-array with shape n x d
        Transformed training data with min 0 and max 1.
    xTest : nd-array with shape m x d
        Transformed test data using same process as training.
    """
    # TODO FILL IN
    df_test_data = pd.DataFrame(xTest)
    df_train_data = pd.DataFrame(xTrain)

    test_information = df_test_data.describe()
    '''
    test_min = test_information.loc['min']

    print("test_min", test_min)

    test_max = test_information.loc['max']

    print("test_max", test_max)

    train_information = df_train_data.describe()
    train_min = train_information.loc['min']

    print("train_min", train_min)

    train_max = train_information.loc['max']

    print("train_max", train_max)
    '''

    for test_column in df_test_data.columns:
        test_min = df_test_data[test_column].describe().loc['min']
        test_max = df_test_data[test_column].describe().loc['max']
        df_test_data[test_column] = (1 / (test_max - test_min)) * df_test_data[test_column] - test_min * (
                1 / (test_max - test_min))

    for train_column in df_train_data.columns:
        train_min = df_train_data[train_column].describe().loc['min']
        train_max = df_train_data[train_column].describe().loc['max']
        df_train_data[train_column] = (1 / (train_max - train_min)) * df_train_data[train_column] - train_min * (
                1 / (train_max - train_min))

    xTest = df_test_data.values
    xTrain = df_train_data.values

    return xTrain, xTest


test_data1 = np.array([[13, 34], [78, 43], [61, 88], [43, 79], [65, 39], [68, 88]])
test_data2 = np.array([23, 54, 74, 42, 61, 28, 83, 39, 62, 23, 61, 18, 20])
print(minmax_range(test_data1,
                   test_data2))


def add_irr_feature(xTrain, xTest):
    """
    Add 2 features using Gaussian distribution with 0 mean,
    standard deviation of 1.

    Parameters
    ----------
    xTrain : nd-array with shape n x d
        Training data
    xTest : nd-array with shape m x d
        Test data

    Returns
    -------
    xTrain : nd-array with shape n x (d+2)
        Training data with 2 new noisy Gaussian features
    xTest : nd-array with shape m x (d+2)
        Test data with 2 new noisy Gaussian features
    """
    # TODO FILL IN
    df_x_test = pd.DataFrame(xTest)
    df_x_train = pd.DataFrame(xTrain)

    irr_feature1_test = np.random.normal(0, 1, df_x_test.shape[0])
    irr_feature2_test = np.random.normal(0, 1, df_x_test.shape[0])

    irr_feature1_train = np.random.normal(0, 1, df_x_train.shape[0])
    irr_feature2_train = np.random.normal(0, 1, df_x_train.shape[0])

    df_x_test.insert(df_x_test.shape[1], 'irr_feature1_test', irr_feature1_test)
    df_x_test.insert(df_x_test.shape[1], 'irr_feature2_test', irr_feature2_test)

    df_x_train.insert(df_x_train.shape[1], 'irr_feature1_train', irr_feature1_train)
    df_x_train.insert(df_x_train.shape[1], 'irr_feature2_train', irr_feature2_train)

    xTrain = df_x_train.values
    xTest = df_x_test.values

    return xTrain, xTest


print("*********")
print(df_test)
print("*********")
print(df_train)
print("*********")
print(add_irr_feature(df_test, df_train))
print("*********")

a = np.array([1, 2, 3, 4, 5, 6, 7])
aP = pd.DataFrame(a)
max = aP.describe().loc['max']
print(type(aP.describe().loc['max']))

scaler = StandardScaler()
a = a.reshape(-1,1)
scaler.fit(a)
result = scaler.transform(a)
print(result)
