# Data Preprocessing

# Importing the libraries
import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer

# Importing the dataset
dataset = pd.read_csv('sales_data.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 3].values

# TODO fill in missing data
imputer = SimpleImputer(strategy=...)
# TODO do not use the whole dataset, but only the last three columns because the first one (country) is not numeric
imputer = imputer.fit(...)
... = imputer.transform(...)
print(X)
