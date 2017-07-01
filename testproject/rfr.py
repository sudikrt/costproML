'''
    Import Libs
'''
import pandas as pd
import numpy as np
from pandas.tools.plotting import scatter_matrix
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

from sklearn.neighbors import KNeighborsClassifier

from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error


#Read Data
dataset = pd.read_csv("damnms.csv")
#print shape
print dataset.shape
#description
print dataset.describe()
#class
print (dataset.groupby('job').size())

print dataset.columns

print dataset.dtypes

print dataset.describe()


columns = dataset.columns.tolist()
columns = [c for c in columns if c not in ["id","job", "place", "cost","lat","lng"]]
target = "cost"

train = dataset.sample(frac = 0.8, random_state = 1)
test = dataset.loc[~dataset.index.isin(train.index)]

print(train.shape)
print(test.shape)

model = LinearRegression()
model.fit(train[columns], train[target])

predictions = model.predict(test[columns])

print test["cost"]
print predictions
print 'Error rate', mean_squared_error(predictions, test[target])
