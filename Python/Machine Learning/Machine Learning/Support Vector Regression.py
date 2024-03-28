# Support Vector Regression does not allow data points near the model line
#  to affect the model, only data points (Slack Variables) OUTSIDE a 
#  certain threshold (Epsilon)

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('Machine Learning\Data1.csv')
#X is every record and every column except the last column (Salary--what we're predicting)
# Since the Level field has already encoded our Position categorical data, we do 
# not need to include the categorical data, or create dummy variables or encoding, so column 0 is excluded
X = dataset.iloc[:,1:-1].values
#Y is the dependent variable (Salary), it's what we're predicting
Y = dataset.iloc[:,-1].values
print(X)
print(Y)

# Y needs to be re-shaped to a 2D array, as a column
Y = Y.reshape(len(Y),1)

# In this example, we do split the data into Training and Test sets
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X
                                                    , Y
                                                    , test_size = 0.2
                                                    , random_state=0)

# Feature Scaling is required in SVR
# Since there are two columns of long data types, we must fit/transform 2 variables
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
sc_Y = StandardScaler()
# fit_transform columns 2 and 3 (level and salary)
X_train = sc_X.fit_transform(X_train)
y_train = sc_Y.fit_transform(y_train)

# Train the SVR model on the whole dataset
# find the rbf Radial Basis Function in the documentation https://scikit-learn.org/stable/modules/svm.html#svm-regression
from sklearn.svm import SVR
regressor = SVR(kernel = 'rbf')
regressor.fit(X_train,y_train)

# Predict the salary Y of a given experience level
# both the scaled values of X and Y must be reversed (inverted)
y_pred = sc_Y.inverse_transform(regressor.predict(sc_X.transform(X_test)).reshape(-1,1))
print(y_pred)

# # Visualize the SVR results
# plt.scatter(sc_X.inverse_transform(X), sc_Y.inverse_transform(Y), color = 'red')
# plt.plot(sc_X.inverse_transform(X), sc_Y.inverse_transform(regressor.predict(X).reshape(-1,1)), color = 'blue')
# plt.title('Salary vs experience with SVR')
# plt.xlabel('Years of Experience')
# plt.ylabel('Salary')
# plt.show()

# # Visualize the SVR results in high resolution
# X_grid = np.arange(min(sc_X.inverse_transform(X)), max(sc_X.inverse_transform(X)),0.1)
# X_grid = X_grid.reshape(len(X_grid),1)
# plt.scatter(sc_X.inverse_transform(X), sc_Y.inverse_transform(Y), color = 'red')
# plt.plot(X_grid, sc_Y.inverse_transform(regressor.predict(sc_X.transform(X_grid)).reshape(-1,1)), color = 'blue')
# plt.title('Truth or Bluff (SVR)')
# plt.xlabel('Position level')
# plt.ylabel('Salary')
# plt.show()

# Determine the R**2 value of the model
#   documentation for R**2 https://scikit-learn.org/stable/modules/generated/sklearn.metrics.r2_score.html#sklearn.metrics.r2_score
from sklearn.metrics import r2_score

print(r2_score(y_test, y_pred))
# R**2 is 0.849, the best R**2 value so far, not great

 
