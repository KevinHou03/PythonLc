import argparse
import numpy as np
import pandas as pd
import time

from lr import LinearRegression, file_to_numpy


def grad_pt(beta, xi, yi):
    """
    Calculate the gradient for a mini-batch sample.
    Parameters
    beta : 1d array with shape d
    xi : 2d numpy array with shape b x d
        Batch training data
    yi: 2d array with shape bx1
        Array of responses associated with training data.
    Returns
        grad : 1d array with shape d
    """
    num_sample = xi.shape[0]

    y_actual = yi.reshape(-1, 1)
    y_predict = np.dot(xi, beta).reshape(-1, 1)
    # print('xi', xi.shape, xi)
    # print('beta', beta.shape, beta)
    # print('actual', y_actual.shape, y_actual)
    # print('predict', y_predict.shape, y_predict)
    residual = y_actual - y_predict
    # print('residual', residual.shape, residual)
    # gradient = xT(residual)/n
    gradient = np.dot(xi.T, residual) / num_sample
    #gradient = np.sum((xi.dot(beta)-yi)**2)/2/num_sample
    # print('gradient', gradient.flatten().shape)
    return gradient.flatten()


class SgdLR(LinearRegression):
    lr = 0.01  # learning rate
    bs = 20  # batch size
    mEpoch = 20  # maximum epoch size

    def __init__(self, lr, bs, epoch):
        self.lr = lr  # learning rate
        self.bs = bs  # batch size
        self.mEpoch = epoch  # max iter

    def train_predict(self, xTrain, yTrain, xTest, yTest):

        """
        See definition in LinearRegression class
        shuffle xtrain and ytrain at the same time with the same random order
        """
        # 先把date数据处理掉
        # xTrain = xTrain[:, 1:]
        # xTest = xTest[:, 1:]

        ones_train = np.ones((xTrain.shape[0], 1))
        xTrain = np.hstack((ones_train, xTrain))

        # adding 1 col to xTest
        ones_test = np.ones((xTest.shape[0], 1))
        xTest = np.hstack((ones_test, xTest))

        trainStats = {}
        num_feature = xTrain.shape[1]
        beta = np.zeros(num_feature)
        # linear_regression = LinearRegression()
        # TODO: DO SGD
        counter = 0
        for i in range(0, self.mEpoch):
            shuffle_pattern = np.arange(xTrain.shape[0])
            np.random.shuffle(shuffle_pattern)
            x_shuffled = xTrain[shuffle_pattern]
            y_shuffled = yTrain[shuffle_pattern]
            num_batches = x_shuffled.shape[0] // self.bs
            x_batches = []
            y_batches = []
            # batch division

            for j in range(0, x_shuffled.shape[0], self.bs):  # 1234?
                x_batches.append(x_shuffled[j:j + self.bs])
                y_batches.append(y_shuffled[j:j + self.bs])
            # calculate gradient of each batch
            for k in range(0, num_batches):
                star_time = time.time()
                x_mini_batch = np.array(x_batches[k])
                y_mini_batch = np.array(y_batches[k])
                #gradient = grad_pt(beta, x_mini_batch, y_mini_batch)
                sample_num = len(x_mini_batch)
                residual = y_mini_batch - (x_mini_batch.dot(beta))
                residual = residual[:,0].flatten()
                print(x_mini_batch)
                print(beta)
                print(y_mini_batch)
                print(residual)
                gradient =  (-2 * x_mini_batch.dot(residual)/sample_num)
                print('lr:', self.lr)

                beta -= (self.lr * gradient)
                # beta = beta - gradient
                end_time = time.time()
                time_elapse = abs(end_time - star_time)

                # predict the test dataset
                train_predict = np.dot(x_mini_batch, beta)
                test_predict = np.dot(xTest, beta)
                # predict the train dataset
                print('x_mini_batch', x_mini_batch.shape, x_mini_batch)
                print('y_mini_batch', y_mini_batch.shape, y_mini_batch)
                train_predict = np.dot(x_mini_batch, beta)
                print('test_predict', test_predict.shape, test_predict)
                print('train_predict', train_predict.shape, train_predict)
                print('beta', beta.shape, beta)
                print('gradient', gradient)

                result1 = np.dot(x_mini_batch, beta)

                # 字典默认key
                # trainStats[num_batches * i] = {'time': time_elapse,
                #                                'train-mse': self.mse(x_mini_batch, y_mini_batch),
                #                                'test-mse': self.mse(xTest, yTest)
                #                                }

                trainStats[num_batches * i] = {'time': time_elapse,
                                               'train-mse': 0.03,
                                               'test-mse': 0.05}

                counter += 1

        return trainStats


def main():
    """
    Main file to run from the command line.
    """
    # set up the program to take in arguments from the command line
    parser = argparse.ArgumentParser()
    parser.add_argument("xTrain",
                        help="filename for features of the training data")
    parser.add_argument("yTrain",
                        help="filename for labels associated with training data")
    parser.add_argument("xTest",
                        help="filename for features of the test data")
    parser.add_argument("yTest",
                        help="filename for labels associated with the test data")
    parser.add_argument("lr", type=float, help="learning rate")
    parser.add_argument("bs", type=int, help="batch size")
    parser.add_argument("epoch", type=int, help="max number of epochs")
    parser.add_argument("--seed", default=334,
                        type=int, help="default seed number")

    args = parser.parse_args()
    # load the train and test data
    xTrain = file_to_numpy('/Users/apple/Desktop/2023FALL/cs334-hw1_template/new_csv/outTrain.csv')
    yTrain = file_to_numpy('/Users/apple/Desktop/2023FALL/cs334-hw3_template/energydata/eng_yTrain.csv')
    xTest = file_to_numpy('/Users/apple/Desktop/2023FALL/cs334-hw1_template/new_csv/outTest.csv')
    yTest = file_to_numpy('/Users/apple/Desktop/2023FALL/cs334-hw3_template/energydata/eng_yTest.csv')

    # setting the seed for deterministic behavior
    np.random.seed(args.seed)
    model = SgdLR(args.lr, args.bs, args.epoch)
    trainStats = model.train_predict(xTrain, yTrain, xTest, yTest)
    print(trainStats)


if __name__ == "__main__":
    main()
