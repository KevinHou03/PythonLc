import argparse
import sys
from collections import Counter

import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.model_selection import train_test_split


def model_assessment(filename):
    """
    Given the entire data, split it into training and test set
    so you can assess your different models
    to compare perceptron, logistic regression,
    and naive bayes.
    """
    dataframe = filename
    # shuffle the data first
    sample_num = dataframe.shape[0]
    indices = np.arange(sample_num)
    np.random.shuffle(indices)
    dataframe = dataframe.iloc[indices].reset_index()
    dataframe.rename(columns={0: 'text'}, inplace=True)
    print(dataframe.columns)
    # sys.exit()
    # now split
    xTrain, xTest = train_test_split(dataframe, test_size=0.3,
                                     random_state=42)  # 0.3 is the commonly used ratio that is believed to generate good result
    # combine the label and the text where label should be in the first column
    # train_data = xTrain.insert(0, '', yTrain)
    # test_data = xTest.insert(0, '', yTest)

    return xTrain, xTest


def build_vocab_map(traindf):
    """
    Construct the vocabulary map such that it returns
    (1) the vocabulary dictionary contains words as keys and
    the number of emails the word appears in as values, and
    (2) a list of words that appear in at least 30 emails.
    {'hello', 4} all the words, and their occurance,
    ---input:
    dataset: pandas dataframe containing the 'text' column
             and 'y' label column

    ---output:
    dict: key-value is word-count pair
    list: list of words that appear in at least 30 emails
    """

    words_dict = {}
    words_over_30 = []
    # first, get rid of the label if it exists
    # combine all elements in each row together
    text_row = traindf.iloc[:, 1].str.cat(sep=' ')
    splitted_list = text_row.split()
    counts = Counter(splitted_list)
    words_dict = dict(counts)

    for key, value in words_dict.items():
        if value >= 30:
            words_over_30.append(key)
    print(len(words_over_30[1:]))

    return words_dict, words_over_30[1:]


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
    for emails_texts in dataset.iloc[:, 1]:
        feat_vector = [1] * freq_size
        splitted = emails_texts.split()
        for index, words in enumerate(freq_words):
            if words not in splitted:
                feat_vector[index] = 0
            if words in splitted:
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
    for emails_texts in dataset.iloc[:, 1]:  # for each email
        feat_vector = [1] * len(freq_words)
        counts = Counter(emails_texts.split())
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


def main():
    """
    Main file to run from the command line.
    """
    # set up the program to take in arguments from the command line
    parser = argparse.ArgumentParser()
    parser.add_argument("--data",
                        default="spamAssassin.data",
                        help="filename of the input data")
    # args = parser.parse_args()
    data = pd.read_csv('/Users/apple/Desktop/2023FALL/CS-334/hw4-template2/spamAssassin.data',header = None)
    # train_data, test_data = model_assessment(args.data)
    # words_dict, words_over_30 = build_vocab_map(train_data)
    # binary_data = construct_binary(train_data,words_over_30)
    # count_data = construct_count(train_data, words_over_30)
    train_data, test_data = model_assessment(data)
    print(train_data.iloc[:,1].shape)


    yTrain_list = []
    for rows in train_data.iloc[:, 1]:
        yTrain_list.append(int(rows.split()[0]))

    yTest_list = []
    for rows in test_data.iloc[:, 1]:
        yTest_list.append(int(rows.split()[0]))

    print('train_data:\n', train_data)

    print('test_data:\n', test_data)

    words_dict, words_over_30 = build_vocab_map(train_data)

    print("length:", len(words_over_30))
    print(words_over_30)

    # print(len(words_dict))
    # print(words_dict)

    binary_train = construct_binary(train_data, words_over_30)
    print("binary", binary_train)
    binary_test = construct_binary(test_data, words_over_30)

    count_train = construct_count(train_data, words_over_30)
    print(count_train)
    count_test = construct_count(test_data, words_over_30)

    binary_train = pd.DataFrame(binary_train)
    binary_train.to_csv('/Users/apple/Desktop/2023FALL/CS-334/binary_train.csv')

    binary_test = pd.DataFrame(binary_test)
    binary_test.to_csv('/Users/apple/Desktop/2023FALL/CS-334/binary_test.csv')

    count_train = pd.DataFrame(count_train)
    count_train.to_csv('/Users/apple/Desktop/2023FALL/CS-334/count_train.csv')

    count_test = pd.DataFrame(count_test)
    count_test.to_csv('/Users/apple/Desktop/2023FALL/CS-334/count_test.csv')

    yTrain_list = pd.DataFrame(yTrain_list)
    yTrain_list.to_csv('/Users/apple/Desktop/2023FALL/CS-334/yTrain.csv')

    yTest_list = pd.DataFrame(yTest_list)
    yTest_list.to_csv('/Users/apple/Desktop/2023FALL/CS-334/yTest.csv')


if __name__ == "__main__":
    main()



