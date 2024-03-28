## Motion Tracking and Object Tracking
# Filtering by Color

import cv2, numpy as np

# initiate webcam
cap = cv2.VideoCapture(0)

# define range of PURPLE color in HSV
lower_purple = np.array([125,0,0])
upper_purple = np.array([175,255,255])

while True:
  ret, frame = cap.read()

  # convert BGR to HSV
  hsv_img = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

  # inRange filters an hsv image and create a mask to capture only values between lower and upper
  mask = cv2.inRange(hsv_img, lower_purple, upper_purple)

  # perform bitwise and on mask and our original frame
  res = cv2.bitwise_and(frame, frame, mask = mask)

  # show all three videos and filters
  cv2_imshow(frame)
  cv2_imshow(mask)
  cv2_imshow(res)

## Gaussian Mixture Background/Foreground Segmentation

import cv2, numpy as np
from google.colab.patches import cv2_imshow

cap = cv2.VideoCapture('walking.avi')

# initiate background subtractor
foreground_background = cv2.BackgroundSubtractorMOG()

while True:

  ret, frame = cap.read()

  # Apply background subtrator to get foreground mask

  foreground_mask = foreground_background.apply(frame)

  cv2_imshow(foreground_mask)


# with webcam input
# try with MOG2 as well
cap = cv2.VideoCapture(0)

foreground_background = cv2.BackgroundSubtractorMOG()

while True:
  ret, frame = cap.read()

  foreground_mask = foreground_background.apply(frame)
  cv2_imshow(foreground_mask)

# improved Gaussian function MOG2
cap = cv2.VideoCapture('walking.avi')

# initiate background subtractor
foreground_background = cv2.BackgroundSubtractorMOG2()

while True:

  ret, frame = cap.read()

  # Apply background subtrator to get foreground mask

  foreground_mask = foreground_background.apply(frame)

  cv2_imshow(foreground_mask)

# foreground Subtraction

cap = cv2.VideoCapture('walking.avi')
ret, frame = cap.read()

#create a float numpy array with frame values
average = np.float32(frame)

while True:
  ret, frame = cap.read()

  # 0.01 is the weight of the image, adjust as needed
  # accumulated weight puts value on objects that are not moving
  cv2.accumulateWeighted(frame, average, 0.01)

  # Scales, calc abs value, converts the result to 8-bit
  background = cv2.convertScaleAbs(average)

  cv2_imshow(frame)
  cv2_imshow(background)


