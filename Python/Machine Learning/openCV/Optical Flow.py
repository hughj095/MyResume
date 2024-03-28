# Optical flow gets the pattern objects in motion in an image between two frames, and shows the distribution of velocities of objects
#   Lucas-Kanade Optical Flow in OpenCV

# Optical Flow

import cv2, numpy as np
from google.colab.patches import cv2_imshow

cap = cv2.VideoCapture('walking.avi')

# set params for corner detection
feature_params = dict(maxCorners = 100,
                      qualityLevel = 0.3,
                      minDistance = 7,
                      blockSize = 7)

# set params for optical flow
lucas_kanade_params = dict(winSize = (15,15),
                           maxLevel = 2,
                           criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))

# create random colors
color = np.random.randint(0,255,(100,3))

######## Dense Optical Flow

import cv2, numpy as np
from google.colab.patches import cv2_imshow

cap = cv2.VideoCapture('walking.avi')

# get frame
ret, first_frame = cap.read()
previous_gray = cv2.cvtColor(first_frame, cv2.COLOR_BGR2GRAY)
hsv = np.zeros_like(first_frame)
hsv[...,1] = 255

while True:
  ret, frame2 = cap.read()
  next = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
  # compute the dense optical flow
  flow = cv2.calcOpticalFlowFarneback(previous_gray, next,
                                      None, 0.5,3,15,3,5,1.2,0)
  # use flow to calculate magnitude (speed) and angle
  magnitude, angle = cv2.cartToPolar(flow[...,0], flow[...,1])
  hsv[...,0] = angle * (180 / (np.pi/2))
  hsv[...,2] = cv2.normalize(magnitude, None, 0, 255, cv2.NORM_MINMAX)
  final = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

  cv2_imshow(final)


  


# make first frame grayscale
ret, prev_frame = cap.read()
prev_gray = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)

prev_corners = cv2.goodFeaturesToTrack(prev_gray, mask = None, **feature_params)

mask = np.zeros_like(prev_frame)

while(1):
  ret, frame = cap.read()
  frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

  #calc optical flow
  new_corners, status, errors = cv2.calcOpticalFlowPyrLK(prev_gray,
                                                         frame_gray,
                                                         prev_corners,
                                                         None,
                                                         **lucas_kanade_params)
  
  # select and store good points
  good_new = new_corners[status==1]
  good_old = prev_corners[status==1]

  # draw the tracks
  for i,(new,old) in enumerate(zip(good_new, good_old)):
    a,b = new.ravel()
    c,d = old.ravel()
    mask = cv2.line(mask, (a,b), (c,d), color[i].tolist(), 2)
    frame = cv2.circle(frame, (a,b), 5, color[i].tolist(), -1)

  img = cv2.add(frame, mask)

  cv2_imshow(img)



  



