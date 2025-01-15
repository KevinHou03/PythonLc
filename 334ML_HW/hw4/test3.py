import pandas as pd

from q1 import *


data = pd.read_csv('/Users/apple/Desktop/2023FALL/CS-334/hw4-template2/spamAssassin.data',header = None)
train_data, test_data = model_assessment(data)
# print(train_data.iloc[:,1].shape)


yTrain_list = []
for rows in train_data.iloc[:, 0]: # rows: 3917  [1, from, mr, joe, mark, email, fax, number, n...
    yTrain_list.append(int(rows[0]))

yTest_list = []
for rows in test_data.iloc[:, 0]:
    yTest_list.append(int(rows[0]))

#modify the train dataset and the test data set so it has two columns, label and text
# for rows in train_data.iloc[1:5,0]:
#     print(rows)
#     print(rows[0:])
#     rows = rows[0:]

train_data['text'] = train_data['text'].apply(lambda x: x[1:])
train_data['label'] = yTrain_list

test_data['text'] = test_data['text'].apply(lambda x: x[1:])
test_data['label'] = yTest_list

total_dict = {}
total_list = []
print(train_data)
for rows in train_data.iloc[1:7,0]:
    total_list.extend(rows)
    # total_dict.update(dict(Counter(rows)))

print(dict(Counter(total_list)))


freq_words = ['hello', 'how', 'are', 'you', 'my', 'friend']
dataset = {'name':['hello', 'chao','feast', 'bay','computer','friend', 'are', 'kevin'],}


dataset = pd.DataFrame(dataset)
print('dataset\n', dataset)

def construct_binary(dataset, freq_words):
    """
    Construct email datasets based on
    the binary representation of the email.
    For each e-mail, transform it into a
    feature vector where the ith entry,
    $x_i$, is 1 if the ith word in the
    vocabulary occurs in the email,
    or 0 otherwise

    ---input:
    dataset: pandas dataframe containing the 'text' column

    freq_word: the vocabulary map built in build_vocab_map() i assume it is a list

    ---output:
    numpy array
    """
    # get rid of the label:
    # dataset = dataset.iloc[:, 1] # comment this if the draindf is just feature values

    # iterate each row (each email)
    freq_size = len(freq_words)
    all_vectors = []
    for emails_texts in dataset.iloc[:, 0]:
        feat_vector = [1] * freq_size
        # splitted = emails_texts.split()
        for index, words in enumerate(freq_words):
            if words not in emails_texts:
                feat_vector[index] = 0
            if words in emails_texts:
                feat_vector[index] = 1
        all_vectors.append(feat_vector)

    all_vectors = np.array(all_vectors)
    binary_data = all_vectors
    print(binary_data.shape)

    return binary_data

def construct_count(dataset, freq_words):
    """
    Construct email datasets based on
    the count representation of the email.
    For each e-mail, transform it into a
    feature vector where the ith entry,
    $x_i$, is the number of times the ith word in the
    vocabulary occurs in the email, feat_vector [i] = dict[words]
    or 0 otherwise

    ---input:
    dataset: pandas dataframe containing the 'text' column

    freq_word: the vocabulary map built in build_vocab_map()

    ---output:
    numpy array
    """
    # get rid of the label: necessary?
    # dataset = dataset.iloc[:, 1] # comment this if the draindf is just feature values

    all_vectors = []
    for emails_texts in dataset.iloc[:, 0]:  # for each email
        feat_vector = [1] * len(freq_words)
        counts = Counter(emails_texts)
        counts_dict = dict(counts)

        for index, words in enumerate(freq_words):
            if words in counts_dict.keys():
                feat_vector[index] = counts_dict[words]
            if words not in counts_dict.keys():
                feat_vector[index] = 0
        all_vectors.append(feat_vector)
    all_vectors = np.array(all_vectors)
    count_data = all_vectors
    print(count_data.shape)

    return count_data


print('binary:\n',construct_binary(dataset,freq_words))
print('count:\n', construct_count(dataset,freq_words))