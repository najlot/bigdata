import numpy as np
from sklearn import linear_model
from sklearn.preprocessing import PolynomialFeatures
import plotly.express as px

# this makes the plot show in the browser even if run from inside PyCharm (without this, the plot does not open)
import plotly.io as pio

pio.renderers.default = 'browser'

# Load the Amazon dataset
dataset = np.loadtxt('amazon_revenue_billion_usd.csv', delimiter=',')

# split into X and y
amazon_X = dataset[:, np.newaxis, 0]
amazon_y = dataset[:, np.newaxis, 1]

# generate plot with input data
fig = px.bar(x=amazon_X.flatten(), y=amazon_y.flatten())

# add some more future x values to get predictions for
amazon_X_pred = np.append(amazon_X, [[2021], [2022], [2023], [2024], [2025]], 0)

# LINEAR REGRESSION
# create linear regression object
regression = linear_model.LinearRegression()

# train the model using the training sets
regression.fit(amazon_X, amazon_y)

# make predictions using the new data points
amazon_y_pred = regression.predict(amazon_X_pred)

# plot outputs
fig.add_scatter(x=amazon_X_pred.flatten(), y=amazon_y_pred.flatten(), name='predictions (linear regression)')

# QUADRATIC REGRESSION
# transform input data into format for quadratic polynomial
poly = PolynomialFeatures(degree=2)
# now transform all data
X = poly.fit_transform(amazon_X)
y = poly.fit_transform(amazon_y)
X_pred = poly.fit_transform(amazon_X_pred)

# with this transformed data, the normal linear regression model can be used
# fit model
regression.fit(X, y)
# make predictions using the new data points
amazon_y_pred_poly = regression.predict(X_pred)

# add another plot
fig.add_scatter(x=amazon_X_pred.flatten(), y=amazon_y_pred_poly[:, 1].flatten(),
                name='predictions (quadratic regression)')

# show the whole plot
fig.show()
