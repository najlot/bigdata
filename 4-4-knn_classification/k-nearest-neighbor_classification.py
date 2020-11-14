import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn import neighbors
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score
from sklearn.model_selection import cross_val_score
import itertools

MAX_NUM_NEIGHBORS = 15
WEIGHTS = 'uniform'
METRIC = 'euclidean'

dataset = pd.read_csv('online_shoppers_intention.csv')

# TODO transform all non-numeric data into numeric data using preprocessing.LabelEncoder()
dataset = ...

# select the last column as label (y)
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

# TODO split dataset into train and test set
X_train, X_test, y_train, y_test = train_test_split(...)

# TODO create classifier and fit to the training set (use MAX_NUM_NEIGHBORS, WEIGHTS and METRIC)
classifier = ...
classifier.fit(...)

# predict test set results
y_pred = classifier.predict(X_test)

# TODO get the F1 score for the predicted test results
print(f1_score(...))