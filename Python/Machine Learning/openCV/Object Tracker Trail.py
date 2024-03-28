# Object Tracker
# This program tracks a defined object by color and draws a trail as you move it in the webcam

import cv2, numpy as np
from google.colab.patches import cv2_imshow

cap = cv2.VideoCapture(0)

# define color range to track
lower_purple = np.array([130,50,90])
upper_purple = np.array([170,255,255])

points = []

ret, frame = cap.read()
Height, Width = frame.shape[:2]
frame_count = 0

while True:
  ret, frame = cap.read()
  hsv_img = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

  # create mask in color range
  mask = cv2.inRange(hsv_img, lower_purple, upper_purple)
  # find contours
  contours, _ = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
                                 cv2.CHAIN_APPROX_SIMPLE)
  # calc centroid
  center = int(Height/2), int(Width/2)

  if len(contours) > 0:
    # get largest contour and its center
    c = max(contours, key=cv2.contourArea)
    (x,y), radius = cv2.minEnclosingCircle(c)
    M = cv2.moments(c)
    try:
      center = (int(M['m10'] / M['m00']), int(M['m01'] / M['m00']))
    except:
      center = int(Height/2), int(Width/2)
    
    # allow only contours with a pixel radius > 25
    if radius > 25:
      # draw circle and leave the last center creating a trail
      cv2.cicle(frame, (int(x), int(y)), int(radius),(0,0,255), 2)
      cv2.circle(frame, center, 5, (0,255,0), -1)
  
  # log center points
  points.append(center)

  # loop over the set of tracked points and draw a line
  if radius > 25:
    for i in range(1, len(points)):
      try:
        cv2.line(frame, points[i-1], points[i], (0,255,0), 2)
      except:
        pass
    frame_count = 0
  else:
    frame_count += 1

    # if we count 10 frames without the object then delete the trail
    if frame_count == 10:
      points = []
      frame_count = 0
    
  # display tracker
  frame = cv2.flip(frame, 1)
  cv2_imshow(frame)
