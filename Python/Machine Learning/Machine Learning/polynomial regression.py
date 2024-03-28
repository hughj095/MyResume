# Polynomial Regression models represents a non-linear model by a power of x
# y = b0 + b1x1 + b2x2**2...

# This example predicts the Salary based on Position and Experience Level from data in Position_Salaries.csv
# and compares to the expected Salary of the interviewee

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv(r'Machine Learning\Data (1).csv')
#X is every record and every column except the last column (Salary--what we're predicting)
# Since the Level field has already encoded our Position categorical data, we do 
# not need to include the categorical data, or create dummy variables or encoding, so column 0 is excluded
X = dataset.iloc[:,:-1].values
#Y is the dependent variable (Salary), it's what we're predicting
Y = dataset.iloc[:,-1].values

# We don't have missing data, so we can skip this step

# We are not including the categorical data in X, so we skip skip this step

# Feature Scaling is not necessary in this data set, so we can skip this

# Spliting the data into Training and Test sets
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,Y,test_size=0.2, random_state=0)

# Training the Polynomial Regression model on the Training set
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
poly_reg = PolynomialFeatures(degree = 4)
X_poly = poly_reg.fit_transform(X_train)
regressor = LinearRegression()
regressor.fit(X_poly, y_train)

# Predicting the Test set results
y_pred = regressor.predict(poly_reg.transform(X_test))
np.set_printoptions(precision=2)
print(np.concatenate((y_pred.reshape(len(y_pred),1), y_test.reshape(len(y_test),1)),1))

# Evaluating the Model Performance
from sklearn.metrics import r2_score
print(r2_score(y_test, y_pred))

# R**2 is 0.945, a very good model so far

# # Visualize the LINEAR Regression Model against the data scatter plot
# plt.scatter(X, Y, color = 'red')
# plt.plot(X, lin_reg.predict(X), color = 'blue')
# plt.title('Truth of Bluff')
# plt.xlabel('Level')
# plt.ylabel('Salary')
# plt.show()

# # Visualize the Polynomial Regression Model against the data scatter plot
# plt.scatter(X, Y, color = 'red')
# plt.plot(X, lin_reg_2.predict(X_poly), color = 'blue')
# plt.title('Truth of Bluff (Polynomial Regression)')
# plt.xlabel('Level')
# plt.ylabel('Salary')
# plt.show()


