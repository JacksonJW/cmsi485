import numpy as np
import pandas as pd
from sklearn import linear_model, preprocessing, tree
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder, KBinsDiscretizer  # noqa: E501
from sklearn.naive_bayes import GaussianNB


COLUMNS = ["age", "work class", "education", "education-num", "marital_status", "occ_code", "relationship", "race", "sex", "cap_gain", "cap_loss", "hours_per_week", "native_country", "income"]  # noqa: E501

# reading training and test data
df_train = pd.read_csv('income-training.csv', names=COLUMNS)
df_test = pd.read_csv('income-test.csv', names=COLUMNS)

# f illing Nan's with -999999
df_train.fillna(-99999)
df_test.fillna(-99999)

le = preprocessing.LabelEncoder()
ohe = OneHotEncoder(sparse=False)
ordinal = OrdinalEncoder()
encoder = le

# fine tuning the data in preprocessing:
for x in COLUMNS:
    if df_train[x].dtypes == 'object':
        df_train_2d = df_train[[x]].copy()
        df_test_2d = df_test[[x]].copy()
        df_train[x] = encoder.fit_transform(df_train_2d)
        df_test[x] = encoder.fit_transform(df_test_2d)

# train the data set
y = df_train.iloc[:, 13]
x = df_train.iloc[:, 1:13]
trainingDataTrained = GaussianNB()
trainingDataTrained.fit(x, y)

# test the accuracy of the trained model with the test dataset
accuracy = trainingDataTrained.score(df_test.iloc[:, 1:13], df_test.iloc[:, 13])  # noqa: E501
print('the accuracy of the trained model is {:.2f}'.format(accuracy*100))
