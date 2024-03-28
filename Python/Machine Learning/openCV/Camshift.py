# CAM shift, Continuosly Adaptive Meanshift uses an adaptive window size that changes sizes and orientation.  It applies meanshift, then calculates the window size
#    and adjusts its position.  Best application for objects that move closer or further away, or change orientation

import cv2, numpy as np
from google.colab.patches import cv2_imshow

# this example tracks purple objects as they enter the track window

cap = cv2.VideoCapture('walking.avi')
ret, frame = cap.read()
print(type(frame))

r, h, c, w = 240, 100, 400, 160
track_window = (c,r,w,h)

roi = frame[r:r+h, c:c+w]

# convert video to hsv
hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

# create a mask for the color bounds
lower_purple = np.array([125,0,0])
upper_purple = np.array([175,255,255])
mask = cv2.inRange(hsv_roi, lower_purple, upper_purple)

# create histogram of the ROI
roi_hist = cv2.calcHist([hsv_roi], [0], mask, [180], [0,180])

# normalize the values to lie between 0 and 255
cv2.normalize(roi_hist, roi_hist, 0, 255, cv2.NORM_MINMAX)

# termination criteria: we stop calculating the centroid after ten iterations
term_crit = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1)

while True:
  ret, frame = cap.read()

  if ret == True:
    # convert to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # calc the probability of each pixel is within the color histogram
    dst = cv2.calcBackProject([hsv], [0], roi_hist, [0,180], 1)
    # apply the mean shift to get the new location
    ret, track_window = cv2.CamShift(dst, track_window, term_crit)


    # use polygons to draw it on the image
    pts = cv2.boxPoints(ret)
    pts = np.int0(pts)
    img2 = cv2.polylines(frame, [pts], True, 255, 2)

    cv2_imshow(img2)

