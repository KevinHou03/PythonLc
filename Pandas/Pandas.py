import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets

'''
Primary panda objects : Series and DataFrame
1.pd.Series is a one-dimensional ndarray with axis labels
'''
# Create a basic series
s = pd.Series(["blue", "red", "green"], name="colors")  # 相当于创造一个column，最后的这个是column的名字
# A dataframe is just a collection of these series
s1 = pd.Series(["blue", "red", "green"], name="colors")  # Create a Series with name "colors"
s2 = pd.Series(["b", "c", "g"], name="first_letter")  # Create another Series with name "first_letter"

# Create a DataFrame by passing a list of Series objects Dataframe不过时一群series
df = pd.DataFrame([s1, s2]).T  # T转置
print(np.shape(df))
print("*********")
print(df)
print("*********")
print(df.describe())  # describe method gives you general statistical information of each column
print("*********")
print(df['colors'].value_counts())  # 这个column所有要素的count
print("*********获得一条column")
print(type(df['first_letter']))  # <class 'pandas.core.series.Series'>
print("*********获得多条column")
print(df[['first_letter', 'colors']])

# 用iris举例
iris_data_sets = datasets.load_iris()
data_set = pd.DataFrame(data=iris_data_sets['data'], columns=iris_data_sets['feature_names'])
data_set.insert(4, column='target', value=iris_data_sets['target'])

print(data_set)  # 打印panda frame dataset
data_set["sepal length (cm)"].hist()  # 做Histgram只能用单列数据，你要输入的是这一列的header
# plt.show() #必须要调用show方法

# 现在我们单取一列，对这一列进行操作
petal_width = data_set["petal width (cm)"]
print(petal_width.min())
print(petal_width.max())
print(petal_width.mean())
print(petal_width.median())

# sort
print(data_set.sort_values(by="sepal length (cm)"))  # 根据sepal length 排序了整个data frame,你也可以在里面嫁一个逗号，然后ascending = True
print("****************")
print(petal_width.sort_values())  # 把这一行单独sort了,按照value值
print("****************")
print(petal_width.sort_index())  # 这个就是根据编号排序，与value大小无关

# 如果我们只想要pedal width大于0.9的值
print("****************")
print(petal_width > 0.9)

# 在整个dataframe里进行这个操作
print("****************")
print((data_set['sepal length (cm)'] > 5.88) & (data_set['petal width (cm)'] < 9.33))

# 继续对某一列操作
print("****************")
print(data_set['sepal length (cm)'])
data_set['sepal length (cm)'] = data_set['sepal length (cm)'] * 10  # 把每个值扩大了十倍
print(data_set['sepal length (cm)'])
# 也可以列x列操作 例如 data_set['sepal length (cm)'] = data_set['sepal length (cm)'] * data_set['sepal length (cm)']


'''
In pandas, the map() function is used to transform values in a Series based on a mapping or a function.
'''
data_set['sepal length (cm)'] = data_set['sepal length (cm)'] / 10  # 先把数据还原


# 首先我们可以简单写一个函数
def classify_sepal_length(sepal_length):
    if sepal_length > 6:
        return "high"
    elif 5 < sepal_length <= 6:
        return "median"
    else:
        return "low"


sepal_length = data_set['sepal length (cm)']
print(data_set['sepal length (cm)'].map(classify_sepal_length)) # 这里直接函数名进去，不用带参数，参数你在前面已经写出来了穿进去的是什么东西


# 更进一步，我们还可以使用count-value获取更多数据
print("****************")
print(data_set['sepal length (cm)'].map(classify_sepal_length).value_counts())
'''
high      61
median    57
low       32
'''


'''

'''
