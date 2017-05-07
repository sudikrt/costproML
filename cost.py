import pandas
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cross_validation import train_test_split
from sklearn.metrics import mean_squared_error

from sklearn.linear_model import LinearRegression

from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from datetime import timedelta
from random import randint
import datetime

from sklearn.cluster import KMeans
#Read data
dateparse = lambda dates: pandas.datetime.strptime(dates, '%Y-%m')
#input_data = pandas.read_csv("input.csv")
input_data = pandas.read_csv("damnm.csv", parse_dates='date', index_col='date', date_parser=dateparse)
print input_data.index
print input_data.shape
print input_data.columns

plt.hist (input_data['pperhour'])
#plt.show()

#Remove any rows without price
input_data = input_data[input_data["pperhour"] > 0]
input_data = input_data.dropna(axis = 0)

print input_data.corr()["pperhour"]

#GET ALL the columsn from dataFrame
columns = input_data.columns.tolist()

#Filter the columns that we dont want
columns = [c for c in columns if c not in ["job", "pperhour"]]

target = "pperhour"

#GENERATE TEST and TRAINING SET
train = input_data.sample(frac=0.8, random_state=1)
test = input_data.loc[~input_data.index.isin(train.index)]

print train.shape
print test.shape

model = LinearRegression()
# Fit the model to the training data.
model.fit(train[columns], train[target])

# Generate our predictions for the test set.
#x = np.array(train[target][:, 1].A1)
predictions = model.predict(test[columns])

#print test
#print predictions
