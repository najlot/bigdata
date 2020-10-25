import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn import tree
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import f1_score
import graphviz

dataset = pd.read_csv('online_shoppers_intention.csv')

# TODO transform all non-numeric data into numeric data using preprocessing.LabelEncoder()
dataset = ...

# select the last column as label (y)
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

# TODO split dataset into train and test set
X_train, X_test, y_train, y_test = train_test_split(...)

# TODO create classifier and fit to the training set
classifier = ...
classifier.fit(...)

# TODO predict test set results
y_pred = ...

# TODO get the F1 score for the predicted test results
print(f1_score(...))

# TODO create tree visualization and dump into file
dot_data = tree.export_graphviz(...)
graph = graphviz.Source(...)
graph.render(...)
