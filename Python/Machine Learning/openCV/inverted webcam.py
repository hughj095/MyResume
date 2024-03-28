## This programs uses your webcam to adjust video to grayscale, blurred, edged and inverted for a cool effect

import cv2
import numpy as np
from google.colab.patches import cv2_imshow

# function to loop through which manipulates image
def sketch(image):
  # convert image to grayscale
  img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  # clean image with guassian blur
  img_gray_blur = cv2.GaussianBlur(img_gray, (5,5), 0)
  # extract edges
  canny_edges = cv2.Canny(img_gray_blur,30,120)
  # do a binary invert
  ret, mask = cv2.threshold(canny_edges,70,255,cv2.THRESH_BINARY_INV)
  return mask

cap = cv2.VideoCapture(0)

while True:
  ret, frame = cap.read()
  cv2_imshow(sketch(frame))
  if cv2.waitkey(1) == 13:
    break

cap.release()
cv2.destroyAllWindows()
