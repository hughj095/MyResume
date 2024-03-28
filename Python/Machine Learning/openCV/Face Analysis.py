### Facial Analysis of President Obama

import cv2, numpy as np
from google.colab.patches import cv2_imshow
import dlib

# model, shape predictor, face detector
PREDICTOR_PATH = 'shape_predictor_68_face_landmarks.dat'
predictor = dlib.shape_predictor(PREDICTOR_PATH)
detector = dlib.get_frontal_face_detector()

# classes for exception handling
class TooManyFaces(Exception):
  pass

class NoFaces(Exception):
  pass

def get_landmarks(im):
  # passes image into function to produce rects, or arrays
  rects = detector(im, 1)

  if len(rects) > 1:
    raise TooManyFaces
  if len(rects) == 0:
    raise NoFaces
  # returns coordinates of landmarks based on dat model
  return np.matrix([[p.x,p.y] 
                       for p in predictor(im, rects[0]).parts()])
  
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

image = cv2.imread('obama.jpg')
landmarks = get_landmarks(image)
image_with_landmarks = annotate_landmarks(image, landmarks)

cv2_imshow(image_with_landmarks)


