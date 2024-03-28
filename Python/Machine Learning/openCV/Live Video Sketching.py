# Live Sketching
# This program is a video filter for video input which returns an inverted binarized video (like a coloring book)

import keras
import cv2, numpy as np
import matplotlib
from google.colab.patches import cv2_imshow

def sketch(image):
  img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  # blur the gray img
  img_gray_blur = cv2.GaussianBlur(img_gray, (5,5), 0)
  # extract edges
  canny_edges = cv2.Canny(img_gray_blur, 20, 50)
  # invert binarize
  ret, mask = cv2.threshold(canny_edges, 70, 255, cv2.THRESH_BINARY_INV)
  return mask

cap = cv2.VideoCapture('walking.avi')


while True:
  ret, frame = cap.read()
  cv2_imshow(sketch(frame))

