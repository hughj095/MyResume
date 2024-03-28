
# Data Preprocessing tools including replacing blanks, transforming categorical data, 
# and Spliting data into Training and Test sets

# This example below uses Data.csv with data showing country, age and salary

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('Machine Learning\Data.csv')
#X is every record and every column except the last column (Purchased--what we're predicting)
X = dataset.iloc[:,:-1].values
#Y is the dependent variable (Purchased), it's what we're predicting
Y = dataset.iloc[:,-1].values

#Replace missing data with average of column
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values=np.nan,strategy='mean')
# Must apply it to the data (fit and transform)
imputer.fit(X[:,1:3])
X[:,1:3] = imputer.transform(X[:,1:3])

# Any categorical data in the dependent or independent variable must be encoded to 1s and 0s before we fit to our model
# In this example we have country data, which must be encoded to a unique 1s and 0s combination
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, LabelEncoder

# X is the entire array and must be transformed to numerical from categorical data
ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [0])],remainder='passthrough')
#fit and transform with this function, then put into array as X
X = np.array(ct.fit_transform(X))

#Encoding the Dependent Variable
le = LabelEncoder()
y = le.fit_transform(Y)


# Splitting Data into Training and Test Sets
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X
                                                    , y
                                                    , test_size = 0.2
                                                    , random_state=0)
print(X_train)
print(y_train)
print(X_test)
print(y_test)

#Feature Scaling to improve performance, and to have all the values of the features in the same range.
#   This is always done AFTER we split the data.  There are two methods, Standardization and Normalization
# Standardization is the value in relation to the mean, divided by the standard dev.
    # This results in data between -3 and 3
# Normalization is the value minus the minimum value in the set, devided by the max minus min
    # This results in data between 0 and 1

from sklearn.preprocessing import StandardScaler

sc = StandardScaler()
# fit_transform columns 4 and 5 (age and salary)
X_train[:, 3:] = sc.fit_transform(X_train[:, 3:])
X_test[:, 3:] = sc.transform(X_test[:,3:])

print(X_train)
print(X_test)



#Z = 0
