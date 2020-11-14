# Simple Linear Regression
# import libraries
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# import dataset
dataset = pd.read_csv('salary_data.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 1].values

# split the dataset into training and test set (use train_test_split(...))
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=1 / 3)

# fit Simple Linear Regression to the training set
learning_algo = LinearRegression()
learning_algo.fit(X_train, y_train)  # this is where the learning happens

# predict the test set results
y_pred = learning_algo.predict(X_test)

# plot the training set results
plt.scatter(X_train, y_train, color='red')
plt.plot(X_train, learning_algo.predict(X_train), color='blue')
plt.title('Salary vs Experience (Training set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

# plot the test set results (similar to training set resolts)
plt.scatter(X_test, y_test)
# plot the trained regression again to compare with the test set
plt.plot(X_train, learning_algo.predict(X_train), color='blue')
plt.title('Salary vs Experience (Test set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

# show the prediction for input "x = 20"
y_pred = learning_algo.predict([[20]])
print(y_pred)
