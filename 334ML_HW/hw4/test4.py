import numpy as np
import pandas as pd

filenames = '/Users/apple/Desktop/2023FALL/CS-334/hw4-template2/spamAssassin.data'
# filename = pd.read_csv(filenames)

# print(filename)
#
# sample_num = filename.shape[0]
# indices = np.arange(sample_num)
# np.random.shuffle(indices)
# filename = filename.iloc[indices].reset_index()

# filename = filename.iloc[indices].reset_index()
# filename.rename(columns={0: 'text'}, inplace=True)
# filename = filename.drop(columns=['index'])
# filename = filename['text'].apply(lambda email: email[0].split())
# print(filename)

#
# dataframe = filename
# # shuffle the data first
# sample_num = filename.shape[0]
# indices = np.arange(sample_num)
# np.random.shuffle(indices)
# filename = filename.iloc[indices].reset_index()
# filename.rename(columns={0: 'text'}, inplace=True)
# filename = filename.drop(columns=['index'])
# filename['text'] = filename['text'].apply(lambda email: email.split())

filename = pd.read_csv('/Users/apple/Desktop/2023FALL/CS-334/hw4-template2/spamAssassin.data', header=None)

# 打乱数据
np.random.seed(0)  # 设置随机种子以确保可重复性
filename = filename.sample(frac=1).reset_index(drop=True)

# 重命名列
filename.rename(columns={0: 'text'}, inplace=True)

# 拆分文本列
filename['text'] = filename['text'].apply(lambda email: email.split())
# filename['text'] = filename['text'].apply(lambda x: x[1:])
print(filename)