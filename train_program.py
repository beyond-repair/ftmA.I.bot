# Import libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error

# Load dataset
# TODO: Load dataset from blockchain

# Split dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Train linear regression model
lin_reg = LinearRegression()
lin_reg.fit(X_train, y_train)

# Train support vector regression model
svr_reg = SVR(kernel='rbf', C=100, gamma=0.1, epsilon=.1)
svr_reg.fit(X_train, y_train)

# Evaluate models
lin_reg_pred = lin_reg.predict(X_test)
lin_reg_mse = mean_squared_error(y_test, lin_reg_pred)
print('Linear Regression MSE:', lin_reg_mse)

svr_reg_pred = svr_reg.predict(X_test)
svr_reg_mse = mean_squared_error(y_test, svr_reg_pred)
print('Support Vector Regression MSE:', svr_reg_mse)

# Save models
# TODO: Save models to file