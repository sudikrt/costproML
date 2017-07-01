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

from math import sin, cos, sqrt, atan2, radians

def finddist (lat1,lon1,lat2,lon2):
    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c
    return distance
#Read Data
dataset = pd.read_csv("damnm.csv", dtype={'supplydemand':'int','cost':'int'})
#print shape
print dataset.shape
#description
print dataset.describe()
#class
print (dataset.groupby('job').size())

print dataset.columns

dataset['lat'] = dataset['lat'].apply(lambda x: str(x))
dataset['lng'] = dataset['lng'].apply(lambda x: str(x))
#dataset['id'] = dataset['id'].apply(pd.to_numeric)
dataset['id'] = dataset['id'].apply(lambda x: int(x))
dataset['cost'] = dataset['cost'].apply(lambda x: int(x))

print dataset.dtypes
'''
print dataset.describe()

columns = dataset.columns.tolist()
job="Tester"
radius=10
df_ = pd.DataFrame()
for index, row in dataset.iterrows():
    if (row["job"] == job):
        df_.append(np.array(row))

print df_

columns = dataset.columns.tolist()
columns = [c for c in columns if c not in ["job", "place", "cost"]]
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


'''
array = dataset.values
X = array[:,3:6]
Y = array[:,6]

print X
validation_size = 0.20
seed = 7
X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, Y, test_size=validation_size, random_state=seed)


knn = SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0,
  decision_function_shape=None, degree=3, gamma='auto', kernel='rbf',
  max_iter=-1, probability=False, random_state=None, shrinking=True,
  tol=0.001, verbose=False)
#knn = KNeighborsClassifier()
knn.fit(X_train, Y_train)
predictions = knn.predict(X_validation)
print(accuracy_score(Y_validation, predictions))
print(confusion_matrix(Y_validation, predictions))
print(classification_report(Y_validation, predictions))
