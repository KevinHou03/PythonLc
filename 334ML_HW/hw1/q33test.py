import argparse
import numpy as np
import pandas as pd
from operator import itemgetter
from collections import Counter

from sklearn.preprocessing import StandardScaler, MinMaxScaler

file_pass1 = '/Users/apple/Desktop/2023FALL/hw1_template/q3xTest.csv'
df_test = pd.read_csv(file_pass1)
print(df_test)

file_pass2 = '/Users/apple/Desktop/2023FALL/hw1_template/q3xTrain.csv'
df_train = pd.read_csv(file_pass2)
print("这是我们来帮助决定class的测试数据:", df_train)

file_pass3 = '/Users/apple/Desktop/2023FALL/hw1_template/q3yTrain.csv'
df_labels_train = pd.read_csv(file_pass3)

file_pass4 = '/Users/apple/Desktop/2023FALL/hw1_template/q3yTest.csv'
df_labels_test = pd.read_csv(file_pass4)
'''
#df_test.insert(2, 'labels', df_labels)
print(df_labels)
print('*********')
print(df_test)
print('*********')

print(df_train.shape[0])
'''
'''
test_sample = df_test.iloc[0]  # get a specific row data
print(test_sample)
train_sample = df_train.iloc[0]
print(train_sample)
distance1 = np.sqrt(np.sum((np.array(test_sample) - np.array(train_sample)) ** 2))
print(distance1)
'''


def euclidean_distance(test_array, train_array):
    # print(type(test_array), type(train_array))
    test = pd.DataFrame(test_array)
    train = pd.DataFrame(train_array)
    result = []
    # print(type(test), type(train))
    for i in range(0, test.shape[0]):
        distance_result = []
        test_target = test.iloc[i]
        for j in range(0, train.shape[0]):
            train_data = train.iloc[j]
            distance = np.sqrt(np.sum((np.array(test_target) - np.array(train_data)) ** 2))
            distance_result.append(distance)
        result.append(distance_result)
    # print(type(result))
    return result


'''
distance_set = euclidean_distance(df_test, df_train)
print("测试数据和训练数据的距离集:", distance_set)
print(len(distance_set) * len(distance_set[0]))
'''

test_array = np.array([[1, 2], [3, 4], [5, 6]])
train_array = np.array([[7, 8], [9, 10], [4, 5]])
distance_set2 = euclidean_distance(test_array, train_array)
print("test for euclidean_distance_raw", distance_set2)


# 这个是传进去一个row(也就是一个单sample） 算这个row到trian data所有点的距离
def euclidean_distance_single(test_data, train):
    # print(type(test_data), type(train))  # two numpy array
    train_dataset = pd.DataFrame(train)
    result = []
    for j in range(0, train.shape[0]):
        train_data = train_dataset.iloc[j]
        distance = np.sqrt(np.sum((np.array(test_data) - np.array(train_data)) ** 2))
        result.append(distance)
    return result


new_result = euclidean_distance_single(test_array[0], train_array)
# 两个参数分别为一个nparray和另一个nparray，第一个是一单行，第二个是一整个train dataset
print("test for euclidean_distance_raw_single", new_result)


# 这个在上一个的基础上，一定要把class带进去，带到result里面去
def euclidean_distance_single_labeled(test_data, train, labels):
    # print(type(test_data), type(train))  # two numpy array
    # test_data = pd.DataFrame(test_data) 这行不应该要
    train_dataset = pd.DataFrame(train)
    train_dataset_labeled = pd.DataFrame(train)
    train_dataset_labeled.insert(2, 'labels', labels)
    # print(train_dataset)
    result = []
    for j in range(0, train.shape[0]):
        train_data = train_dataset.iloc[j]  # train_data without label
        train_data_labeled = train_dataset_labeled.iloc[j]
        distance = np.sqrt(np.sum((np.array(test_data) - np.array(train_data)) ** 2))
        result.append([distance, train_data_labeled['labels']])
    return result


result_labeled = euclidean_distance_single_labeled(df_test, df_train, df_labels_train)
print(result_labeled)
print(len(result_labeled))
sorted_list = sorted(result_labeled, key=itemgetter(0))
print(sorted_list)
class_list = [t[1] for t in sorted_list[0:999]]
print(class_list)
'''
for index, value in enumerate(sorted_list):
    while index != 4:
        class_list.append(value[1])

print(class_list)
'''
'''
count = Counter(class_list)
element = count.most_common(1)[0][0]
print(element)
'''
print("以下是对accuracy的测试")
print("测试组标签：", df_labels_test)
print("训练组标签：", df_labels_train)


def accuracy(test_label, train_label):
    correctness_counter = 0
    for number, value in enumerate(test_label):
        if test_label[number] == train_label[number]:
            correctness_counter += 1
    return correctness_counter / len(test_label)


tester = [0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1]
tester_series = pd.Series(tester)
trainer = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
trainer_series = pd.Series(trainer)
# print(accuracy(tester, trainer))
print("accuracy test:", accuracy(tester_series, trainer_series))

'''
test case for euclidean_single_labeled
'''

test_array2 = np.array([[1, 2], [3, 4], [5, 6]])
train_array2 = np.array([[7, 8], [9, 10], [4, 5]])
label2 = np.array(['0', '1', '0'])
print(euclidean_distance_single(test_array2[0], train_array2))
print(euclidean_distance_single_labeled(test_array2[0], train_array2, label2))

'''
test data:
0     5.277959   7.337077
1     3.220191   1.425023
2    14.034404   4.622037
3    24.374362   6.965873
4     6.585567  10.713930

train data:
0     5.277959   7.337077
1     3.220191   1.425023
2    14.034404   4.622037
3    24.374362   6.965873
4     6.585567  10.713930
'''


def predict(self, xFeat):
    """
    Given the feature set xFeat, predict
    what class the values will have.

    Parameters
    ----------
    xFeat : nd-array with shape m x d
        The data to predict.

    Returns
    -------
    yHat : 1d array or list with shape m
        Predicted class label per sample
    """
    yHat = []  # variable to store the estimated class label
    xFeat = pd.DataFrame(xFeat)
    # TODO
    # for subject in xFeat.values:
    # xFeat.shape[0]-1
    for i in range(0, xFeat.shape[0] - 1):  # 这里是取出了test集里面的每一个元素，并拿test里的每一个元素和train中所有元素算距离
        subject = xFeat.values[i]
        # distance_list = euclidean_distance_single_labeled(xFeat.values[i], self.x_train_data,
        # self.class_labels_train)
        train_dataset = pd.DataFrame(self.x_train_data)
        train_dataset_labeled = pd.DataFrame(self.x_train_data)
        train_dataset_labeled.insert(2, 'labels', self.class_labels_train)
        result = []
        for j in range(0, self.x_train_data.shape[0]):
            train_data = train_dataset.iloc[j]
            train_data_labeled = train_dataset_labeled.iloc[j]
            distance = np.sqrt(np.sum((np.array(xFeat.values[i]) - np.array(train_data)) ** 2))
            result.append([distance, train_data_labeled['labels']])  # now the result stores a bunch of 1 and 0s
        result = sorted(result, key=itemgetter(0))
        # print(distance_list_sorted)
        marked_target = [t[1] for t in result[0:self.k]]
        print("train_data_labeled:", marked_target)
        counter = Counter(marked_target)
        most_common = counter.most_common(1)[0][0]
        # print("most common:", most_common)
        yHat.append(most_common)
        # print("yHat:", yHat)

    return yHat


def euclidean_distance_single_labeled(test_data, train, labels):
    # print(type(test_data), type(train))  # two numpy array
    # test_data = pd.DataFrame(test_data)
    train_dataset = pd.DataFrame(train)
    train_dataset_labeled = pd.DataFrame(train)
    train_dataset_labeled.insert(2, 'labels', labels)
    # print(train_dataset)
    result = []
    for j in range(0, train.shape[0]):
        train_data = train_dataset.iloc[j]  # train_data without label// train_data is a dataframe
        train_data_labeled = train_dataset_labeled.iloc[j]
        distance = np.sqrt(np.sum((np.array(test_data) - np.array(train_data)) ** 2))
        result.append([distance, train_data_labeled['labels']])
    return result


# np.argsort test
a = np.array([1, 4, 3, 2])
a = np.argsort(a)
print(a) # 0312 按照大小的index排的

# can i do a list[list]?
list1 = [1,2,3]
list2 = list[list1]
print(list2)
