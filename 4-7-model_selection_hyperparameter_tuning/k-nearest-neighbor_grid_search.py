import pandas as pd
from sklearn import preprocessing
from sklearn import neighbors
from sklearn.model_selection import train_test_split, GridSearchCV

MAX_NUM_NEIGHBORS = 15

dataset = pd.read_csv('online_shoppers_intention.csv')

# TODO transform all non-numeric data into numeric data using preprocessing.LabelEncoder()
dataset = ...

# select the last column as label (y)
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

# TODO split dataset into train and test set
X_train, X_test, y_train, y_test = train_test_split(...)

# TODO add parameters as a dictionary like this: {'parameter_name': [possible_value1, possible_value2]}
parameters = [{
    'n_neighbors': ...,
    'weights': ...,
    'metric': ...
}]

# TODO instantiate classifier object
estimator = ...
# generate grid search object with classifier object
grid_search = GridSearchCV(estimator=estimator,
                           param_grid=parameters,
                           scoring='f1_macro',
                           cv=10,
                           n_jobs=-1)
# TODO run grid search on dataset
grid_search = grid_search.fit(...)
best_score = grid_search.best_score_
best_parameters = grid_search.best_params_

print('optimized F1 score: ' + str(best_score))
print('optimized parameters: ' + str(best_parameters))
