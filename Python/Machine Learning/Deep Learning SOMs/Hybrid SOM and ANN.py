# This file build an unsupervised DL model with a SOM, then with a supervised DL model ANN, it predicts the probability
#   that the customer will commit credit card fraud

### Part 1: Build the SOM to detect fraud

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

## Importing the dataset

dataset = pd.read_csv('Credit_Card_Applications.csv')
X = dataset.iloc[:, :-1].values 
y = dataset.iloc[:, -1].values

## Feature Scaling
# scales values in X between 0 and 1
from sklearn.preprocessing import MinMaxScaler
sc = MinMaxScaler(feature_range = (0,1))
X = sc.fit_transform(X)

# Training the SOM

from minisom import MiniSom
som = MiniSom(x=10, y=10, input_len= 15, sigma= 1.0, learning_rate = 0.5)
# must initialize the weights
som.random_weights_init(X)
som.train_random(data = X, num_iteration = 100)

# Visualize the Results

from pylab import bone, pcolor, colorbar, plot, show
bone()
pcolor(som.distance_map().T)
colorbar()
markers = ['o', 's']
colors = ['r', 'g']
for i, x in enumerate(X):
    w = som.winner(x)
    plot(w[0] + 0.5,
         w[1] + 0.5,
         markers[y[i]],
         markeredgecolor = colors[y[i]],
         markerfacecolor = 'None',
         markersize = 10,
         markeredgewidth = 2)
show()

# Finding the Fraud

mappings = som.win_map(X)
frauds = np.concatenate((mappings[(1,1)], mappings[(4,1)]), axis = 0)
frauds = sc.inverse_transform(frauds)

print('Fraud Customer IDs')
for i in frauds[:, 0]:
  print(int(i))

###### Part 2: build an ANN to predict probability of fraud

customers = dataset.iloc[:, 1:].values

is_fraud = np.zeros(len[dataset])

#Creates the dependent variable for each customer ID whether they committed fraud or not (training data)
for i in range(len[dataset]):
    if dataset.iloc[i,0] in frauds:
        is_fraud[i] = 1

# Feature Scaling - must apply in Machine Learning
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
customers = sc.fit_transform(customers)

# Initialize the ANN
import keras
ann = keras.models.Sequential()

# Add the input layer and first hidden layer
# units are the number of fields in the dataset used to calculate the output, but it can be arbituary
# "relu" is the rectifier activation function: y=max(x,0)
ann.add(keras.layers.Dense(units=6, activation='relu'))

# Add second hidden layer
ann.add(keras.layers.Dense(units=6, activation='relu'))

# Add output layer (output field is binary, so units = 1) (using sigmoid in the output layer returns a probability as well)
# when predicting multiple categories (non-binary output) use the softmax activation function
ann.add(keras.layers.Dense(units=1, activation='sigmoid'))

# Compile the ANN
# The "adam" optimizer conducts stoichastic gradient disscent in updating the weights
# if computing a binary output, you must use binary_crossentropy, if not use categorical cross-entropy
ann.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

# Training the ANN on the training set
# classic batch size is 32 in ML
# only need 1 batch size and 2 epochs in this scenario because there are only a few fraud examples in the input dataset
ann.fit(customers, is_fraud, batch_size = 1, epochs = 2)

# Predict prob of fraud by customer id
y_pred = ann.predict(customers)
y_pred = np.concatenate((dataset.iloc[:,0:1], y_pred), axis = 1).values

# sorted probs high to low
y_pred = y_pred[y_pred[:,1].argsort()]


