import numpy as np
import sklearn
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import SGDRegressor
import matplotlib.pyplot as plt
from lr import LinearRegression, file_to_numpy, mse

# xTrain = file_to_numpy('/Users/apple/Desktop/2023FALL/CS-334/cs334-hw1_template/new_csv/outTest.csv')
# yTrain = file_to_numpy('/Users/apple/Desktop/2023FALL/CS-334/cs334-hw3_template/energydata/eng_yTrain.csv')
# xTest = file_to_numpy('/Users/apple/Desktop/2023FALL/CS-334/cs334-hw1_template/new_csv/outTrain.csv')
# yTest = file_to_numpy('/Users/apple/Desktop/2023FALL/CS-334/cs334-hw3_template/energydata/eng_yTest.csv')


print(sklearn.__version__)
# Load the diabeteprint(sklearn.__version__)s dataset
data = load_diabetes()

# Split the dataset into features and target
X = data.data
y = data.target

# Split the data into training and test sets
xTrain, xTest, yTrain, yTest = train_test_split(X, y, test_size=0.2, random_state=42)

# Define a range of learning rates and batch sizes to explore
learning_rates = np.linspace(0.00001, 0.1, 20)
batch_sizes = [1, len(xTrain) // 100, len(xTrain) // 10, len(xTrain)]

# Initialize lists to store results
results = []

for lr in learning_rates:
    for bs in batch_sizes:
        # Initialize and fit the SGDRegressor
        sgd_regressor = SGDRegressor(max_iter=1000, tol=1e-3, random_state=42, learning_rate='constant', eta0=lr)
        sgd_regressor.fit(xTrain, yTrain)

        # Calculate mean squared error on the test set
        mse = np.mean((sgd_regressor.predict(xTest) - yTest) ** 2) / 3000

        # Store the results
        results.append((lr, bs, mse))

# Separate results into batches based on batch size
result_batches = {bs: [] for bs in batch_sizes}
for lr, bs, mse in results:
    result_batches[bs].append((lr, mse))

# Create separate plots for each batch size
for bs, data in result_batches.items():
    lrs, mses = zip(*data)
    plt.plot(lrs, mses, color='blue')


plt.xlabel('lr')
plt.ylabel('Train MSE')
plt.title('Training MSE vs. Lr')
plt.legend()
plt.show()
