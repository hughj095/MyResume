###### Car and person detection in videos
import cv2, numpy as np
from google.colab.patches import cv2_imshow

# create classifer
body_classifer = cv2.CascadeClassifier('haarcascade_fullbody.xml')

# load video
cap = cv2.VideoCapture('walking.avi')

# loop through video images
while cap.isOpened():
  # read first frame
  ret, frame = cap.read()
  frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_LINEAR)
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  # pass frame through body classifer (the 3 value is minimum neighbors; adjust as needed)
  bodies = body_classifer.detectMultiScale(gray, 1.2, 3)
  # draw rectangle for any bodies identified
  for (x,y,w,h) in bodies:
    cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,255),2)
    cv2_imshow(frame)


# Car Detection

import cv2, numpy as np
import time
from google.colab.patches import cv2_imshow

# create classifier
car_classifier = cv2.CascadeClassifier('haarcascade_car.xml')

# load video
cap = cv2.VideoCapture('cars.avi')

while cap.isOpened():
  # read first frame
  # slow video speed with time.sleep
  # time.sleep(0.1)
  ret, frame = cap.read()
  frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_LINEAR)
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  # pass frame through body classifer (the 3 value is minimum neighbors; adjust as needed)
  cars = car_classifier.detectMultiScale(gray, 1.2, 3)
  # draw rectangle for any bodies identified
  for (x,y,w,h) in cars:
    cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,255),2)
    cv2_imshow(frame)

