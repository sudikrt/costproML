import pandas
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

#Read data
games = pandas.read_csv("game.csv")

print games.columns

print games.shape

plt.hist (games["average_rating"])

plt.show ()

games[games["average_rating"] == 0]

#print games[games["average_rating"] == 0].iloc[0]

#print(games[games["average_rating"] == 0].iloc[0])
# Print the first row of all the games with scores greater than 0.
#print(games[games["average_rating"] > 0].iloc[0])


# Remove any rows without user reviews.
games = games[games["users_rated"] > 0]
# Remove any rows with missing values.
games = games.dropna(axis=0)

print games.corr()["average_rating"]


# Get all the columns from the dataframe.
columns = games.columns.tolist()
# Filter the columns to remove ones we don't want.
columns = [c for c in columns if c not in ["bayes_average_rating", "average_rating", "type", "name"]]

# Store the variable we'll be predicting on.
target = "average_rating"


# Generate the training set.  Set random_state to be able to replicate results.
train = games.sample(frac=0.9, random_state=1)
# Select anything not in the training set and put it in the testing set.
test = games.loc[~games.index.isin(train.index)]
# Print the shapes of both sets.
print(train.shape)
print(test.shape)


model = LinearRegression()
# Fit the model to the training data.
model.fit(train[columns], train[target])

# Generate our predictions for the test set.
x = np.array(train[target][:, 1].A1)
predictions = model.predict(test[columns])

fig, ax = plt.subplots(figsize=(12,8))
ax.plot(x, predictions, 'r', label='Prediction')
ax.scatter(data.Population, data.Profit, label='Traning Data')
ax.legend(loc=2)
ax.set_xlabel('Population')
ax.set_ylabel('Profit')
ax.set_title('Predicted Profit vs. Population Size')

# Compute error between our test predictions and the actual values.

print mean_squared_error(predictions, test[target])

print test["average_rating"]
print predictions
print 'Error rate', mean_squared_error(predictions, test[target])
