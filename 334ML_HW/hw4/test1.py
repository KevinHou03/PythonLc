from collections import Counter

import pandas as pd
import numpy as np


# Creating a DataFrame from a dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 30, 22, 35, 28],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Miami']
}

df = pd.DataFrame(data)

print(df)

sample_num = df.shape[0]
indices = np.arange(sample_num)
np.random.shuffle(indices)
df = df.iloc[indices].reset_index()

print(df)

combined_text = df.iloc[:,1].str.cat(sep=' ')
print(combined_text)
splitted = combined_text.split()
print(splitted)

word_list = ['hello', 'hello', 'hello','good', 'good', 'good','bitch']

counts = Counter(word_list)
counts_dict = dict(counts)
print(counts_dict)

list2 = []

for key,values in counts_dict.items():
    if values == 1:
        list2.append(key)

print(list2)


print(df)
for i in range(0,df.shape[0]):
    row = df.iloc[i,:]
    print(row)


data = {
    'Name': ['Alice loves u ', 'Bob loves me ', 'Charlie loves her', 'David loves her father', 'Eve hates steve'],
}
df2 = pd.DataFrame(data)
print(df2)

freq_words = ['loves','u']
freq_size = len(freq_words)
all_vectors = []
for i in df2.iloc[:,0]:
    feat_vector = [1] * freq_size
    splitted = i.split()
    print(splitted)
    for index, words in enumerate(freq_words):
        print(index,words)
        if words not in splitted:
            feat_vector[index] = 0
        if words in splitted:
            feat_vector[index] = 1
    print(feat_vector)
    all_vectors.append(feat_vector)

all_vectors = np.array(all_vectors)
print(all_vectors)

for emails_texts in df2.iloc[:, 0]:  # for each email
    counts = Counter(emails_texts.split())
    counts_dict = dict(counts)
    print(counts_dict)

# print(type(splitted))
# for word in word_list:
#     print(word)
#     counts = Counter(word)
#     print(counts)

import sys
for line in sys.stdin:
    count = 0
    for i in range(0,int(line)+1):
        if i % 5 != 0 and i % 7 != 0:
            count += i
    print(count)




