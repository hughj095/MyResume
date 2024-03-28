# Photo Restoration
# This program restores a digital photo of Abraham Lincoln
# it removes tear lines in the original photo and blends the surrounding pixels

import cv2, numpy as np
from google.colab.patches import cv2_imshow

image = cv2.imread('abraham.jpg')

# (manually) create a mask of damaged areas in grayscale.  The mask is a white line or shape drawn in the areas which you want to blend or restore.
marked_damages = cv2.imread('mask.jpg',0)

# make all non-marked area black
#  the mask is denoted by a white line(s) (255)  All other colors (254 and below) are made black.
ret, thresh1 = cv2.threshold(marked_damages, 254, 255, cv2.THRESH_BINARY)

# Dilate (make bigger) the mask lines
kernel = np.ones((7,7), np.uint8)
mask = cv2.dilate(thresh1, kernel, iterations=1)

restored = cv2.inpaint(image, mask, 3.0, 0, cv2.INPAINT_TELEA)
cv2_imshow(restored)
