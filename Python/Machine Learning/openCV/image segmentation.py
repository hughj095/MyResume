# Image Segmentation
# Contours are boundaries
import cv2, numpy as np
from google.colab.patches import cv2_imshow

#Load and make grayscale (must make grayscale else error)
image = cv2.imread('shapes.jpg')
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

#find canny edges
canny = cv2.Canny(gray,30,200)

#find contours
#RETR is a retrieval mode, use retr_external or retr_list
contours, hierarchy = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
#make contours yellow
cv2.drawContours(image, contours, -1, (0,255,0), 3)
cv2_imshow(image)

######## Sorting Contours, sorting shapes by size
import cv2, numpy as np
from google.colab.patches import cv2_imshow

image = cv2.imread('bunchofshapes.jpg')

#Create a blank image
blank_image = np.zeros((image.shape[0], image.shape[1], 3))

#grayscale the original
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

#find the edges of the grayscale
edged = cv2.Canny(gray, 30, 120)

#calculate the array of the contours
contours, hierarchy = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

#apply the contours to the blank image
cv2.drawContours(blank_image, contours, -1, (0,255,0), 3)

#apply the contours to the original
cv2.drawContours(image, contours, -1, (0,255,0), 3)

#make a function to return the areas of each shape in a list
def get_contour_areas(contours):
  all_areas = []
  for cnt in contours:
    area = cv2.contourArea(cnt)
    all_areas.append(area)
  return all_areas

#load the original image
image = cv2.imread('bunchofshapes.jpg')

# sort contours large to small
sorted_contours = sorted(contours, key=cv2.contourArea, reverse=True)

print(get_contour_areas(sorted_contours))

###### Find Approximate contours when they are not well defined
import cv2, numpy as np
from google.colab.patches import cv2_imshow

image = cv2.imread('house.jpg')
orig_image = image.copy()

# make gray and binary
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)

#find contours
contours, hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

# loop through each contour and compute the bounding rectangle
for c in contours:
  x,y,w,h = cv2.boundingRect(c)
  cv2.rectangle(orig_image, (x,y), (x+w,y+h), (0,0,255), 2)
  #cv2_imshow(orig_image)

# loop through each contour and compute the approximate contour
for c in contours:
  # adjust the accuracy value as a test
  accuracy = 0.03 * cv2.arcLength(c, True)
  approx = cv2.approxPolyDP(c, accuracy, True)
  cv2.drawContours(image, [approx], 0, (0,255,0), 2)
  cv2_imshow(image)

# loop through each contour and compute the convex hull (smallest polygon that encloses the object)
for c in contours:
  hull = cv2.convexHull(c)
  cv2.drawContours(image, [hull], 0, (0,255,0), 2)
  cv2_imshow(image)

############ Matching shape contours
import cv2, numpy as np
from google.colab.patches import cv2_imshow

#Load the reference shape
template = cv2.imread('4star.jpg')

#Load target image of shapes with shape we're trying to match
target = cv2.imread('shapestomatch.jpg')
target_gray = cv2.cvtColor(target, cv2.COLOR_BGR2GRAY)

#Threshold both images before finding contours
ret, thresh1 = cv2.threshold(template, 127, 255, 0)
ret, thresh2 = cv2.threshold(target_gray, 127, 255, 0)

#Find contours in template
contours, hierarchy = cv2.findContours(thresh2,cv2.RETR_LIST, 
                                       cv2.CHAIN_APPROX_NONE)

#Sort the contours by area in order to remove that with the largest 
# contour which is the image outline
sorted_contours = sorted(contours, key=cv2.contourArea, reverse=True)

#We extract the second largest contour which will be our template contour
template_contour = contours[1]

#Extract contours from second target image
contours, hierarchy = cv2.findContours(thresh2, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

for c in contours:
  # loop through as use cv2.matchShapes()
  match = cv2.matchShapes(template_contour, c, 1, 0.0)
  # if the match value is less than 0.15, it's a match
  if match < 0.15:
    closest_contour = c
  else:
    closest_contour = []

cv2.drawContours(target, [closest_contour], -1, (0,255,0), 3)
cv2.imshow(target)

###### Identify Shapes with names
import cv2, numpy as np
from google.colab.patches import cv2_imshow

from numpy.core.numeric import count_nonzero
image = cv2.imread("someshapes.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#reverse the gray image with threshold
ret, thresh = cv2.threshold(gray,127,255,1)

#Extract contours as array
contours, hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

#Loop through each contours and identify each shape by number of sides (approx), then label and color
for cnt in contours:
  #get approximate polygons
  approx = cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt,True), True)
  if len(approx) == 3:
    shape_name = "triangle"
    cv2.drawContours(image, [cnt], 0, (0,255,0), -1)
    #Find contour center to place text at center
    M = cv2.moments(cnt)
    cx = int(M['m10'] / M['m00'])
    cy = int(M['m01'] / M['m00'])
    cv2.putText(image, shape_name, (cx-50,cy), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 1)

  elif len(approx) == 4:
    x,y,w,h = cv2.boundingRect(cnt)
    M = cv2.moments(cnt)
    cx = int(M['m10'] / M['m00'])
    cy = int(M['m01'] / M['m00'])

    # check if square else rectangle
    if abs(w-h) <= 3:
      shape_name = "Square"
      #find contour center to place text at center
      cv2.drawContours(image, [cnt], 0, (0,125,255), -1)
      cv2.putText(image, shape_name, (cx-50,cy), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 1)
    else:
      shape_name = "Rectangle"
      #find center to place text
      cv2.drawContours(image, [cnt], 0, (0,0,255), -1)
      M = cv2.moments(cnt)
      cx = int(M['m10'] / M['m00'])
      cy = int(M['m01'] / M['m00'])
      cv2.putText(image, shape_name, (cx-50, cy), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 1)

  elif len(approx) == 10:
    shape_name = "star"
    cv2.drawContours(image, [cnt], 0, (255,255,0), -1)
    M = cv2.moments(cnt)
    cx = int(M['m10'] / M['m00'])
    cy = int(M['m01'] / M['m00'])
    cv2.putText(image, shape_name, (cx-50, cy), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 1)
  elif len(approx) >= 15:
    shape_name = "circle"
    cv2.drawContours(image, [cnt], 0, (0,255,255), -1)
    M = cv2.moments(cnt)
    cx = int(M['m10'] / M['m00'])
    cy = int(M['m01'] / M['m00'])
    cv2.putText(image, shape_name, (cx-50, cy), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 1)

cv2_imshow(image)

#### Line Detection with Houghlines
import cv2, numpy as np
from google.colab.patches import cv2_imshow

image = cv2.imread('soduku.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 100, 170, apertureSize = 3)

#adjust the last perameter 240 for accuracy
lines = cv2.HoughLines(edges, 1, np.pi / 180, 240)

for [[rho, theta]] in lines:
  a = np.cos(theta)
  b = np.sin(theta)
  x0 = a * rho
  y0 = b * rho
  x1 = int(x0 + 1000 * (-b))
  y1 = int(y0 + 1000 * (a))
  x2 = int(x0 - 1000 * (-b))
  y2 = int(y0 - 1000 * (a))
  cv2.line(image, (x1,y1), (x2,y2), (255, 0,0), 2)

cv2_imshow(image)



#### Probabalistic Houghlines
import cv2, numpy as np
from google.colab.patches import cv2_imshow

image = cv2.imread('soduku.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 100, 170, apertureSize = 3)

# np.pi / 180 is 1 degree in a circle
lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 100, 5, 10)

for [[x1, y1, x2, y2]] in lines:
  cv2.line(image, (x1, y1), (x2, y2), (0,255,0), 3)

cv2_imshow(image)

####### Blob detection
import cv2, numpy as np
from google.colab.patches import cv2_imshow

image = cv2.imread('Sunflowers.jpg', cv2.IMREAD_GRAYSCALE)

# set detector as Class
detector = cv2.SimpleBlobDetector_create()

keypoints = detector.detect(image)

#draw blobs as red circles
blank = np.zeros((1,1))
blobs = cv2.drawKeypoints(image, keypoints, blank, (0,255,255),
                          cv2.DrawMatchesFlags_DEFAULT)

cv2_imshow(blobs)

####### Counting circles and ellipses
import cv2, numpy as np
from google.colab.patches import cv2_imshow

image = cv2.imread('blobs.jpg', 0)

detector = cv2.SimpleBlobDetector_create()
keypoints = detector.detect(image)

# draw blobs as red circles
blank = np.zeros((1,1))
blobs = cv2.drawKeypoints(image, keypoints, blank, (0,0,255), cv2.DrawMatchesFlags_DRAW_RICH_KEYPOINTS)

# place text on image with count of blobs
number_of_blobs = len(keypoints)
text = f"total number of blobs:" + str(len(keypoints))
cv2.putText(blobs, text, (20,550), cv2.FONT_HERSHEY_SIMPLEX, 1, (100, 0, 255), 2)

cv2_imshow(blobs)

####### Now distinguish between circles and ellipses
params = cv2.SimpleBlobDetector_Params()

# Filter by object area in pixels
params.filterByArea = True
params.minArea = 100

# Filter by circularity
params.filterByCircularity = True
params.minCircularity = 0.9

# Filter by convexity
params.filterByConvexity = True
params.minConvexity = 0.2

# filter by inertia (measure of ellipticalness: low is more elliptical, high is more circular)
params.filterByInertia = True
params.minInertiaRatio = 0.01

# use SimpleBlobDetector_create class
detector = cv2.SimpleBlobDetector_create(params)
keypoints = detector.detect(image)

# return a 1x1 array and use it to draw a red circle over the circle blobs
blank = np.zeros((1,1))
blobs = cv2.drawKeypoints(image, keypoints, blank, (0,0,255), cv2.DrawMatchesFlags_DRAW_RICH_KEYPOINTS)

# count number of circles detected and write text in image
number_of_blobs = len(keypoints)
text = f"total number of circles: " + str(len(keypoints))
cv2.putText(blobs, text, (20,550), cv2.FONT_HERSHEY_SIMPLEX, 1, (100, 0, 255), 2)

cv2_imshow(blobs)



  













