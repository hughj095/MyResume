# This ANN predicts which of 10000 bank customers are a highest risk 
#   of leaving the bank


import numpy as np
import pandas as pd
import tensorflow as tf

#Import Dataset
dataset = pd.read_csv('/Machine Learning Deep Learning/Churn_Modelling.csv')
X = dataset.iloc[:, 3:-1].values
y = dataset.iloc[:, -1].values

print(X)
print(y)

# Encode Categorical Data
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
X[:, 2] = le.fit_transform(X[:, 2])

# One Hot Encoding the Geography column [1]
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [1])], remainder='passthrough')
X = np.array(ct.fit_transform(X))

# Split data into Training and Test Sets
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Feature Scaling - must apply in Machine Learning
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Initialize the ANN
ann = tf.keras.models.Sequential()

# Add the input layer and first hidden layer
# units are the number of fields in the dataset used to calculate the output, but it can be arbituary
# "relu" is the rectifier activation function: y=max(x,0)
ann.add(tf.keras.layers.Dense(units=6, activation='relu'))

# Add second hidden layer
ann.add(tf.keras.layers.Dense(units=6, activation='relu'))

# Add output layer (output field is binary, so units = 1) (using sigmoid in the output layer returns a probability as well)
# when predicting multiple categories (non-binary output) use the softmax activation function
ann.add(tf.keras.layers.Dense(units=1, activation='sigmoid'))

# Compile the ANN
# The "adam" optimizer conducts stoichastic gradient disscent in updating the weights
# if computing a binary output, you must use binary_crossentropy, if not use categorical cross-entropy
ann.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

# Training the ANN on the training set
# classic batch size is 32 in ML
ann.fit(X_train, y_train, batch_size = 32, epochs = 100)

# Print the prediction of a single observation (France, score 600, Male
#   40 years old, Balance 60k, has 2 products, yes credit card, yes active member, estimated salary 50k)
#   input of the "predict" method must be in a 2D array [[double brackets]]
#   must be scaled/tranformed
#   sigmoid prediction produces a probability.  Or if less than 0.5, customer will most likely stay with the bank.
print(ann.predict(sc.transform([[1, 0, 0, 600, 1, 40, 3, 60000, 2, 1, 1, 50000]])) > 0.5)
#   result is FALSE, therefore probability of leaving the bank is low.

# Predict the Test Set Results
y_pred = ann.predict(X_test)
y_pred = (y_pred > 0.5)
print(np.concatenate((y_pred.reshape(len(y_pred),1), y_test.reshape(len(y_test),1)),1))

# Make the confusion Matrix
from sklearn.metrics import confusion_matrix, accuracy_score
cm = confusion_matrix(y_test, y_pred)
print(cm)
accuracy_score(y_test, y_pred)
