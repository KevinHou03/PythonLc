import pandas as pd
from matplotlib import pyplot as plt
from sklearn.preprocessing import StandardScaler
import seaborn as sns


def extract_features(df):
    """
    Given a pandas dataframe, extract the relevant features
    from the date column

    Parameters
    ----------
    df : pandas dataframe
        Training or test data
    Returns
    -------
    df : pandas dataframe
        The updated dataframe with the new features
    """
    # TODO do more than this
    # 1/11/16 17:00
    date = df['date']
    date = pd.to_datetime(date, format='%m/%d/%y %H:%M')
    # year = date.dt.year
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
    return df


def select_features(df):
    """
    Select the features to keep

    Parameters
    ----------
    df : pandas dataframe
        Training or test data
    Returns
    -------
    df : pandas dataframe
        The updated dataframe with a subset of the columns
    """
    # TODO
    # corr = df.corr()
    # corr_feat_target = corr.iloc[:, -1]
    # corr_feat_feat = corr.iloc[:-1, :-1]
    #
    # features_to_remove1 = corr_feat_target[abs(corr_feat_target) < 0.5].index
    # df.drop(columns=features_to_remove1, inplace=True)
    #
    # features_to_remove2 = corr_feat_feat[abs(corr_feat_feat) > 0.85].index
    # df.drop(columns=features_to_remove2, inplace=True)  # removed both
    # # 第一次被删除的特征在第二次会被忽略

    Corr = df.corr()
    for columns, values in Corr.iloc[-1, :].items():
        if abs(value) < 0.3:
            df = df.drop(columns = [column])



def preprocess_data(trainDF, testDF):
    '''
    what else? handle missing data?

    '''
    """
    Preprocess the training data and testing data

    Parameters
    ----------
    trainDF : pandas dataframe
        Training data
    testDF : pandas dataframe
        Test data
    Returns
    -------
    trainDF : pandas dataframe
        The preprocessed training data
    testDF : pandas dataframe
        The preprocessed testing data
    """
    # TODO do something
    # trainDF = extract_features(trainDF)
    # trainDF = select_features(trainDF)
    # trainDF.fillna(0, inplace=True)
    #
    # testDF = extract_features(testDF)
    # testDF = select_features(testDF)
    # testDF.fillna(0, inplace=True)

    # Use StandardScaler to scale the data
    scale = StandardScaler()
    trainDF.iloc[:, 1:] = scale.fit_transform(trainDF.iloc[:, 1:])
    # use eth same scaler
    testDF.iloc[:, 1:] = scale.transform(testDF.iloc[:, 1:])

    return trainDF, testDF


df = pd.read_csv('/Users/apple/Desktop/2023FALL/cs334-hw3_template/energydata/eng_xTrain.csv')
df = extract_features(df)
corr = df.corr()
print(corr)
print(df)
df = select_features(df)
print(df)

# plt.figure(figsize=(8, 8))
# sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f", annot_kws={"size": 4}, cbar_kws={"shrink": 0.7})
#
# plt.title('Correlation Matrix Heatmap')  # Add a title to the heatmap
# plt.show()

for column, value in corr.iloc[-1,:].items():
    print(column)
    print(value)


