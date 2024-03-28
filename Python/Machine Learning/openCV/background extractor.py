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

