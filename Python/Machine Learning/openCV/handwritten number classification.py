# Handwritten Digit Classification
# this program inputs a MNIST CNN model to predict five handwritten numbers

from keras.datasets import mnist
from keras.models import load_model
import cv2, numpy as np
from google.colab.patches import cv2_imshow

classifier = load_model('MNIST_keras_CNN.h5')

(x_train, y_train), (x_test, y_test) = mnist.load_data()

def draw_test(name, pred, input_in):
  BLACK = [0,0,0]
  expanded_image = cv2.copyMakeBorder(input_in, 0,0,0,imageL.shape[0],
                                      cv2.BORDER_CONSTANT, value = BLACK)
  expanded_image = cv2.cvtColor(expanded_image, cv2.COLOR_GRAY2BGR)
  cv2.putText(expanded_image, str(pred), (122,75), cv2.FONT_HERSHEY_COMPLEX_SMALL,
              3,(0,255,0), 1)
  cv2_imshow(expanded_image)

for i in range(0,10):
  rand = np.random.randint(0,len(x_test))
  input_in = x_test[rand]

  imageL = cv2.resize(input_in, None, fx=4, fy=4, interpolation = cv2.INTER_CUBIC)
  cv2_imshow(imageL)
  input_in = input_in.reshape(1,28,28,1)

  # get prediction
  res = str(classifier.predict(input_in, 1, verbose=0)[0])
  draw_test("Prediction", res, imageL)

###### Test Classifer on Image
from preprocessors import x_coord_contour, makeSquare, resize_to_pixel

image = cv2.imread('numbers.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5,5), 0)
edged = cv2.Canny(blurred, 30,150)

_, contours. _ = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours = sorted[contours, key = x_cord_contour, reverse = False]

full_number = []

for c in contours:
  # compute bounding box
  (x,y,w,h) = cv2.boundingRect(c)
  if w >=5 and h >= 25:
    roi = blurred[y:y + h, x:x+w]
    ret, roi = cv2.threshold(roi, 127, 255, cv2.THRESH_BINARY_INV)
    roi = makeSquare(roi)
    roi = resize_to_pixel(28,roi)
    cv2_imshow(roi)
    roi = roi / 255.0
    roi = roi.reshape(1,28,28,1)

    # get prediction
    res = str(classifier.predict_classes(roi, 1, verbose=0)[0])
    full_number.append(res)
    cv2.rectangle(image, (x.y), (x+w,y+h), (0,0,255), 2)
    cv2.putText(image, res, (x,y+155), cv2.FONT_HERSHEY_COMPLEX,2,(255,0,0),2)
    cv2_imshow(image)




