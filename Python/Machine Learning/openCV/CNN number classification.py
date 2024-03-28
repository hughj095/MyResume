# CNN in Keras with mnist hand-written number data set to predict the number of the handwritten number

from keras.datasets import mnist
from google.colab.patches import cv2_imshow



(x_train, y_train), (x_test, y_test) = mnist.load_data()

# im_show 6 images from x_train

import cv2
import numpy as np
from google.colab.patches import cv2_imshow

for i in range(0,6):
  random = np.random.randint(0,len(x_train))
  img = x_train[random]
  cv2_imshow(img)

# show 6 images using matplotlib

import matplotlib.pyplot as plt

plt.subplot(331)
random_num = np.random.randint(0,len(x_train))
plt.imshow(x_train[random_num], cmap=plt.get_cmap('gray'))


# prepare dataset for training

# store the number of rows and columns
img_rows = x_train[1].shape[0]
img_cols = x_train[0].shape[0]

# change shape from 3D to 4D using reshape (required by keras)
# dimensions are Samples, Rows, Cols, Depth
x_train = x_train.reshape(x_train.shape[0], img_rows, img_cols, 1)
x_test = x_test.reshape(x_test.shape[0], img_rows, img_cols, 1)

# img is grayscale, so use 3 if colored img
input_shape = (img_rows, img_cols, 1)

# keras inputs float32
x_train = x_train.astype('float32')
x_test = x_test.astype('float32')

# normalize by dividing by 255, bringing values to 0 to 1
x_train /= 255
x_test /= 255

# One Hot Encoding for categorical data labels

from keras.utils import to_categorical

y_train = to_categorical(y_train)
y_test = to_categorical(y_test)

# Create Model
import keras
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D
from keras import backend as K
from keras.optimizers import SGD

model = Sequential()

model.add(Conv2D(32, kernel_size=(3,3),
                 activation='relu',
                 input_shape=input_shape))

model.add(Conv2D(64,(3,3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.25))
model.add(Flatten())
model.add(Dense(120, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(10,
                activation='softmax'))

model.compile(loss= 'categorical_crossentropy',
              optimizer = SGD(0.01),
              metrics = ['accuracy'])

print(model.summary())


# Train Model

batch_size = 32
epochs = 1

history = model.fit(x_train,
                    y_train,
                    batch_size = batch_size,
                    epochs = epochs,
                    verbose = 1,
                    validation_data = (x_test,y_test))

score = model.evaluate(x_test, y_test, verbose = 0)

print(score[0], score[1])



# Plot Loss and Accuaracy

import matplotlib.pyplot as plt


history_dict = history.history

loss_values = history_dict['loss']
val_loss_values = history_dict['val_loss']
epochs = range(1,len(loss_values) + 1)

line1 = plt.plot(epochs, val_loss_values, label = 'Validation/Test Loss')
line2 = plt.plot(epochs, loss_values, label = 'Training Loss')
plt.setp(line1, linewidth=2.0, marker = '+', markersize=10.0)
plt.setp(line2, linewidth=2.0, marker = '4', markersize=10.0)
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.grid(True)
plt.legend()
plt.show()

# Save Model and Load Model

model.save('8_mnist_simple_cnn_1_epoch.h5')
model.save('8_mnist_simple_cnn_1_epoch.keras')

from keras.models import load_model

classifier = load_model('8_mnist_simple_cnn_1_epoch.h5')

# Input some test data into the new model called classifer

import cv2, numpy as np

def draw_test(name, pred, input_im):
  BLACK = [0,0,0]
  expanded_image = cv2.copyMakeBorder(input_im,0,0,0, imageL.shape[0], cv2.BORDER_CONSTANT, value=BLACK)
  expanded_image = cv2.cvtColor(expanded_image, cv2.COLOR_GRAY2BGR)
  cv2.putText(expanded_image, str(pred), (152,70), cv2.FONT_HERSHEY_COMPLEX_SMALL, 4, (0,255,0), 2)
  cv2_imshow(expanded_image)

for i in range(0,10):
  rand = np.random.randint(0,len(x_test))
  input_im = x_test[rand]

  imageL = cv2.resize(input_im, None, fx=1, fy=4, interpolation = cv2.INTER_CUBIC)
  input_im = input_im.reshape(1,28,28,1)

  # get prediction
  res = str(classifier.predict(input_im))

  draw_test('Prediction', res, imageL)


# Make a diagram of model architecture as model_plot.png
from tensorflow.keras.utils import plot_model

model_diagram_path = ""

plot_model(model, to_file = model_diagram_path + "model_plot.png",
           show_shapes = True,
           show_layer_names = True)

img = cv2.imread(model_diagram_path + 'model_plot.png')
plt.figure(figsize = (30,15))
imgplot = plt.imshow(img)
