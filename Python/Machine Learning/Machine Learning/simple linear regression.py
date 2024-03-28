# Simple Linear Regression Model with salary and years of experience data

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('Machine Learning\Salary_Data.csv')
#X is every record and every column except the last column (Salary--what we're predicting)
X = dataset.iloc[:,:-1].values
#Y is the dependent variable (Salary), it's what we're predicting
Y = dataset.iloc[:,-1].values

# We don't have missing data, so we can skip this step
# We don't have categorical data, so we can skip this step

# Split the data into training and test sets
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X
                                                    , Y
                                                    , test_size = 0.2
                                                    , random_state=1)

# Train the simple linear regression model on the training set
from sklearn.linear_model import LinearRegression

regressor = LinearRegression()
regressor.fit(X_train,y_train)

# Predict the salary y of the test set X
y_pred = regressor.predict(X_test)

# Visualize the Training Set
plt.scatter(X_train, y_train, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('Salary vs experience (Training Set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

# Visualize the Test Set
plt.scatter(X_test, y_test, color = 'red')
# do not replace regression line model from training
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('Salary vs experience (Test Set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

#Make a single prediction of salary with one data point (12 years of exp) provided
#The double brackets is for a 2D array--which the predict method expects
print(regressor.predict([[12]]))

#What are the model coefficents if we wanted to write the equation
print(regressor.coef_) # Slope
print(regressor.intercept_) # Y Intercept
