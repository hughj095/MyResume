# Multiple Linear Regression equation is y= b0 + b1X1 + b2X2 + b3X3
# where you have one y intercept and multiple slope coefficients and multiple independent variablesj

# This example takes data from 50 startups and using each company's 
# R&D spend, Admin, and Marketing spend, determines the Profit

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv(r'Machine Learning\Data (1).csv')
#X is every record and every column except the last column (Profit--what we're predicting)
X = dataset.iloc[:,:-1].values
#Y is the dependent variable (Profit), it's what we're predicting
Y = dataset.iloc[:,-1].values

# We don't have missing data, so we can skip this step

# # We have categorical data (State), so we need to create dummy variables for these
# from sklearn.compose import ColumnTransformer
# from sklearn.preprocessing import OneHotEncoder
# # X is the entire array and must be transformed to numerical from categorical data
# ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [3])],remainder='passthrough')
# #fit and transform with this function, then put into array as X
# X = np.array(ct.fit_transform(X))

# Split the data into training and test sets
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X
                                                    , Y
                                                    , test_size = 0.2
                                                    , random_state=0)

# Feature Scaling is not necessary in Multiple Linear Regression, so we can skip this

# Train the multiple linear regression model on the training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train,y_train)

# Predict the salary y of the test set X
y_pred = regressor.predict(X_test)
# displays decimals to the hundredths place ($.$$ profit)
np.set_printoptions(precision = 2)

# Print the predicted Profit values and compare to the Test Profit values
# reshape is used to display the vector vertically (as columns)
print(np.concatenate((y_pred.reshape(len(y_pred),1),y_test.reshape(len(y_pred),1)),1))

# Determine a single Profit value with given variables: R&D 160k, Admin 130k
# , and Marketing 300k in California (California is 1,0,0 in the categorical data transform)
# print(regressor.predict([[1, 0, 0, 160000, 130000, 300000]]))

# Get the final Multiple Linear Regression Equation
print(regressor.coef_)
print(regressor.intercept_)

# Therefore Profit = 86.6*State1 - 873*State2 + 786*State3 + 0.773*R&D
#   + 0.0329*Admin + 0.0366*Marketing + 42467.52

# Determine the R**2 value of the model
#   documentation for R**2 https://scikit-learn.org/stable/modules/generated/sklearn.metrics.r2_score.html#sklearn.metrics.r2_score
from sklearn.metrics import r2_score

print(r2_score(y_test, y_pred))

# R**2 value is 0.932, a very good model

