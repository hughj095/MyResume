# this program inputs handwritten numbers 0-9 in a training set and predicts the written number
#   with machine learning algorithm KNN

import cv2, numpy as np
from google.colab.patches import cv2_imshow

import cv2, numpy as np
from google.colab.patches import cv2_imshow
print(cv2.__version__)

image = cv2.imread('digits.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# pyramid down function is for scaling the image down
small = cv2.pyrDown(image)

# split the image into 5000 cells, each 20x20 size
#   this outputs a 4D array (50 x 100 x 20 x 20)
cells = [np.hsplit(row, 100) for row in np.vsplit(gray,50)]

#convert to numpy array
x = np.array(cells)

# split into training data and test data by 70:30
train = x[:,:70].reshape(-1,400).astype(np.float32)
test = x[:,70:100].reshape(-1,400).astype(np.float32)

# labels for training and test set
k = [0,1,2,3,4,5,6,7,8,9]
train_labels = np.repeat(k,350)[:,np.newaxis]
test_labels = np.repeat(k,150)[:,np.newaxis]

# initiate KNN, train the data, test the data
# ret is a boolean if the function successfully ran
knn = cv2.ml.KNearest_create()
knn.train(train, train_labels)
ret, result, neighbors, distance = knn.find_nearest(test, k=3)

# check accuracy
# matches is the boolean if there were results
matches = result == test_labels
correct = np.count_nonzero(matches)
accuracy = correct * (100.0 / result.size)
print(accuracy)


