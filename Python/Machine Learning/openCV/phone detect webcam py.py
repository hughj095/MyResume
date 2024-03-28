###### Mini Project Object Detection with SIFT to identify phone in webcam
####      Be sure to work locally to access your webcam
import cv2, numpy as np
from google.colab.patches import cv2_imshow

def sift_detector(new_image, image_template):
# function that compares input to template
  image1 = cv2.cvtColor(new_image, cv2.COLOR_BGR2GRAY)
  image2 = image_template

  sift = cv2.SIFT()

# obtain keypoints
  keypoints_1, descriptors_1 = sift.detectAndCompute(image1, None)
  keypoints_2, descriptors_2 = sift.detectAndCompute(image2, None)

# determine parameters of flann
  FLANN_INDEX_KDTREE = 0
  index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 3)
  search_params = dict(checks = 100)

# create Flann matcher object
  flann = cv2.FlannBasedMatcher(index_params, search_params)

# obtain matches with K nearest neighbor
  matches = flann.knnMatch(descriptors_1, descriptors_2, k=2)

# good matches are a list of all matches for memory
# matches are used to detect and identify a match within the webcam
  good_matches = []
  for m,n in matches:
    if m.distance < 0.7 * n.distance:
      good_matches.append(m)

  return len(good_matches)

cap = cv2.VideoCapture(0)

image_template = cv2.imread('box_in_scene.png', 0)

while True:
  # get webcam images
  ret, frame = cap.read()
  # get height and width of webcam frame
  height, width = frame.shape[:2]

  # define ROI box dimensions
  top_left_x = width / 3
  top_left_y = (height / 2) + (height / 4)
  bottom_right_x = (width / 3) * 2
  bottom_right_y = (height / 2) - (height / 4)

  # draw rectangle for region of interest ROI
  cv2.rectangle(frame, (top_left_x, top_left_y),
   (bottom_right_x, bottom_right_y), 255, 3)

  # crop window of observation
  cropped = frame[bottom_right_y:top_left_y , top_left_x:bottom_right_x]

  # flip frame horizontally
  frame = cv2.flip(frame, 1)

  # get number of SIFT matches
  matches = sift_detector(cropped, image_template)

  # display status string showing the current number of matches
  cv2.putText(frame, str(matches),(450,450), cv2.FONT_HERSHEY_COMPLEX, 2,
              (0,255,0), 3)
  
  # adjust threshold of keypoints to detect objects more or less like the template
  threshold = 10

  # if matches exceed threshold then object is detected
  if matches > threshold:
    cv2.rectangle(frame, (top_left_x,top_left_y), (bottom_right_x, 
                                                   bottom_right_y),
                                                  (0,255,0),3)
    cv2.putText(frame, "Object Found", (50,50), cv2.FONT_HERSHEY_COMPLEX,
                2,(0,255,0), 2)
  
  cv2_imshow(frame)
    
