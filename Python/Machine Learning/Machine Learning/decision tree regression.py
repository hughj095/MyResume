# Regression Trees splits the scatter plot into sections, then uses an algorythm to predict the Y value
# Decision Trees are not good for 2D data models.  They are better for 3D and above.

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('Machine Learning\Data1.csv')
#X are the experience levels
X = dataset.iloc[:, :-1].values
#Y is the dependent variable (Salary), it's what we're predicting
Y = dataset.iloc[:,-1].values

# In this example, we do split the data into Training and Test sets
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X
                                                    , Y
                                                    , test_size = 0.2
                                                    , random_state=0)

# Feature Scaling is not required in Decision Tree Regression or Random Forest Regression, so skip this

# Train the Decision Tree model on the whole dataset
from sklearn.tree import DecisionTreeRegressor
# The max_depths is proportional to the number of outliers the model takes into account (lower is better)
regressor = DecisionTreeRegressor(random_state = 0)
regressor.fit(X,Y)

# Predict salary at level 6.5 (as a 2D array)
y_pred = regressor.predict(X_test)
print(y_pred)

# # Plot
# X_grid = np.arange(min(X), max(X),0.1)
# X_grid = X_grid.reshape(len(X_grid),1)
# plt.scatter(X,Y, color = 'red')
# plt.plot(X_grid, regressor.predict(X_grid), color = 'blue')
# plt.title('Decision Tree Regression')
# plt.xlabel('Position level')
# plt.ylabel('Salary')
# plt.show()

# Determine the R**2 value of the model
#   documentation for R**2 https://scikit-learn.org/stable/modules/generated/sklearn.metrics.r2_score.html#sklearn.metrics.r2_score
from sklearn.metrics import r2_score

print(r2_score(y_test, y_pred))