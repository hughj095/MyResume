####### Find Where's Waldo

import cv2, numpy as np
from google.colab.patches import cv2_imshow

image = cv2.imread('WaldoBeach.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Load template Waldo to compare
template = cv2.imread('waldo.jpg',0)

# Match template Waldo to main image and identify coordinates of matched template over the image
results = cv2.matchTemplate(gray, template, cv2.TM_CCOEFF)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(results)

# Draw a red rectangle over the template Waldo over the matched location
top_left = max_loc
bottom_right = (top_left[0] + 50, top_left[1] + 50)
cv2.rectangle(image, top_left, bottom_right, (0,0,255), 5)

cv2_imshow(image)

######### corner detection using goodFeaturestoTrack()
img = cv2.imread('chess.JPG')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

corners = cv2.goodFeaturesToTrack(gray, 50, 0.01, 15)

# loop through each corner and draw a rectangle around it
for corner in corners:
  x, y = corner[0]
  x = int(x)
  y = int(y)
  cv2.rectangle(img, (x-10, y-10), (x+10, y+10), (0,255,0), 2)

cv2_imshow(img)

######## Conduct Object detection using the five methods (SIFT, SURF, FAST, BRIEF, and ORB)

import cv2, numpy as np
from google.colab.patches import cv2_imshow

####### SIFT feature detection (fails with Google Colab)
image = cv2.imread('input.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

sift = cv2.SIFT()
keypoints = sift.detect(gray, None)

image = cv2.drawKeypoints(image, keypoints, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

print(f'number of keypoints detected = {len(keypoints)}')

cv2_imshow(image)


####### SURF feature detection (not a module in python 3.10)
image = cv2.imread('input.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

surf = cv2.SURF()
# Only values larger than the hessian Threshold will be retained by the detector
surf.hessianThreshold = 7500
keypoints, descriptors = surf.detectAndCompute(gray, None)

image = cv2.drawKeypoints(image, keypoints, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

print(f'number of keypoints detected = {len(keypoints)}')

cv2_imshow(image)


######## FAST (fails with Google Colab)
image = cv2.imread('input.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

fast = cv2.FastFeatureDetector()
keypoints = fast.detect(gray, None)

image = cv2.drawKeypoints(image, keypoints, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

#print(f'number of keypoints detected = {len(keypoints)}')

cv2_imshow(image)

########## BRIEF (no DescriptorExtractor_create in python 3.10 cv2)
image = cv2.imread('input.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

fast = cv2.FastFeatureDetector()

brief = cv2.DescriptorExtractor_create("BRIEF")

keypoints = fast.detect(gray, None)

keypoints, descriptors = brief.compute(gray, keypoints)

image = cv2.drawKeypoints(image, keypoints, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

#print(f'number of keypoints detected = {len(keypoints)}')

cv2_imshow(image)


######### ORB (Oriented Fast and Rotated Brief) (Also crashes in Google Colab)
image = cv2.imread('input.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# ORB specifies the number of keypoints you want (1000)
orb = cv2.ORB(1000)
keypoints = orb.detect(gray, None)
keypoints, descriptors = orb.compute(gray, keypoints)

image = cv2.drawKeypoints(image, keypoints, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

#print(f'number of keypoints detected = {len(keypoints)}')

cv2_imshow(image)


