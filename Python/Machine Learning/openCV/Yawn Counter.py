# This file inputs your webcam video and counts and displays the number of times you yawn!

import cv2, numpy as np
from google.colab.patches import cv2_imshow
import dlib

PREDICTION_PATH = "shape_predictor_68_face_landmarks.dat"
predictor = dlib.shape_predictor(PREDICTION_PATH)
detector = dlib.get_frontal_face_detector()

def get_landmarks(im):
  rects = detector(im, 1)

  if len(rects) > 1:
    return "error"
  if len(rects) == 0:
    return "error"
  return np.matrix([[p.x, p.y] for p in predictor(im, rects[0]).parts()])

def annotate_landmarks(im, landmarks):
  im = im.copy()
  for idx, point in enumerate(landmarks):
    pos = (point[0,0], point[0,1])
    cv2.putText(im, str(idx), pos,
                fontFace = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,
                fontScale=0.4,
                color = (0,0,255))
    cv2.circle(im, pos, 3, color=(0,255,255))
  return im

def top_lip(landmarks):
  # uses the landmarks and extracts the top lip landmark mean
  top_lip_pts = []
  for i in range(50,53):
    top_lip_pts.append(landmarks[i])
  for i in range(61,64):
    top_lip_pts.append(landmarks[i])
  top_lip_all_pts = np.squeeze(np.asarray(top_lip_pts))
  top_lip_mean = np.mean(top_lip_pts, axis = 0)
  return int(top_lip_mean[:,1])

def bottom_lip(landmarks):
  # same for bottom lip
  bottom_lip_pts = []
  for i in range(65,68):
    bottom_lip_pts.append(landmarks[i])
  for i in range(56,59):
    bottom_lip_pts.append(landmarks[i])
  bottom_lip_all_pts = np.squeeze(np.asarray(bottom_lip_pts))
  bottom_lip_mean = np.mean(bottom_lip_pts, axis=0)
  return int(bottom_lip_mean[:,1])

def mouth_open(image):
  # determine lip distance
  landmarks = get_landmarks(image)

  if landmarks == "error"
    return image, 0
  
  image_with_landmarks = annotate_landmarks(image, landmarks)
  top_lip_center = top_lip(landmarks)
  bottom_lip_center = bottom_lip(landmarks)
  lip_distance = abs(top_lip_center - bottom_lip_center)
  return image_with_landmarks, lip_distance

cap = cv2.VideoCapture(0)
yawns = 0
yawn_status = False

while True:
  ret, frame = cap.read()
  image_landmarks, lip_distance = mouth_open(frame)

  prev_yawn_status = yawn_status

  # if lip distance is greater than 20 pixels, then subject is yawning....could also be a proportion of face size
  if lip_distance > 20:
    yawn_status = True

    cv2.putText(frame, "Subject is Yawning", (50,450),
                cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255),2)
    
    output_text = "Yawn Count:" + str(yawns+1)

    cv2.putText(frame, output_text, (50,50),
                cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,127), 2)
    
  else: yawn_status = False

  if prev_yawn_status == True and yawn_status == False:
    yawns += 1
  
  cv2_imshow(image_landmarks)
  cv2_imshow(frame)

