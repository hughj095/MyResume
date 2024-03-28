# Transformations are geometric distortions used to correct distortions and perspective issues
#    types are Affine (Scale, rotate, translate).  Parallels maintain themselvs.
#    and Non-Affine (homography, distort by shape axes)

# Translations (shifting an image) requires a translation matrix and the cv2.warpAffine() function

# Rotation use a matrix of sin and cos, and the angle of rotation using cv2.getRotationMatrix2D()

#######Translation

import cv2
import numpy as np

image = cv2.imread('input.jpg')

# store height and width
height, width = image.shape[:2]

quarter_height, quarter_width = height/4, width/4

# T is the translation matrix

T = np.float32([[1,0, quarter_width], [0,1,quarter_height]])

# use warpAffine() to translate using matrix T
img_translation = cv2.warpAffine(image, T, (width,height))
cv2_imshow(img_translation)

######## Rotation
rotation_matrix = cv2.getRotationMatrix2D((width/2, height/2), 90, 1)

rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height))

cv2_imshow(rotated_image)

# Transpose the image to adjust scale
rotated_image = cv2.transpose(image)
cv2_imshow(rotated_image)


####### Scaling and Resizing
import cv2
import numpy as np

image = cv2.imread('input.jpg')

# make image 3/4 of original size
image_scaled = cv2.resize(image, None, fx=0.75, fy =0.75)
#cv2_imshow(image_scaled)

# now double the size
img_scaled = cv2.resize(image, None, fx=2, fy=2, interpolation = cv2.INTER_CUBIC)
#cv2_imshow(img_scaled)

# Resize by exact dimensions
img_scaled = cv2.resize(image, (900, 400), interpolation = cv2.INTER_AREA)
cv2_imshow(img_scaled)


# Image Pyramids are useful when scaling images
# pyrDown reduces scale to 50%
# pyrUp upscales pixels, but could cause blurring
smaller = cv2.pyrDown(image)
larger= cv2.pyrUp(smaller)
cv2_imshow(image)
cv2_imshow(smaller)
cv2_imshow(larger)

##### Cropping images

height, width = image.shape[:2]
# get pixel coordinates top left for cropping
start_row, start_col = int(height * .25), int(width * .25)

# get bottom right coord for end cropping
end_row, end_col = int(height * .75), int(width * .75)

# use indexing to crop the image
cropped = image[start_row:end_row , start_col:end_col]

cv2_imshow(cropped)

###### Arithmetic Operations to adjust brightness

import cv2
import numpy as np
from google.colab.patches import cv2_imshow

image = cv2.imread("input.jpg")

# create a matrix of ones, then multiply it by a scalar of 100
M = np.ones(image.shape, dtype = "uint8") * 75

# then add the matrix to the image to increase brightness
added = cv2.add(image, M)
cv2_imshow(added)

# likewise subtract for darker
subtracted = cv2.subtract(image, M)
cv2_imshow(subtracted)

# Making shapes
# Make a Square
import cv2
import numpy as np
from google.colab.patches import cv2_imshow

square = np.zeros((300,300), np.uint8)
cv2.rectangle(square, (50,50), (250,250), 255, -2)
cv2_imshow(square)

# Make an ellipse
ellipse = np.zeros((300,300), np.uint8)
cv2.ellipse(ellipse, (150,150), (150,150), 30, 0, 180, 255, -1)
cv2_imshow(ellipse)

# Bitwise Operations

# show where the two shapes (square and ellipse) intersect
And = cv2.bitwise_and(square, ellipse)
cv2_imshow(And)

# where the two are either (or)
Or = cv2.bitwise_or(square, ellipse)
cv2_imshow(Or)

# where either exist by themself
Xor = cv2.bitwise_xor(square, ellipse)
cv2_imshow(Xor)

# everything that isn't part of the square
Not_sq = cv2.bitwise_not(square)
cv2_imshow(Not_sq)

# Convolution is a math operation performed
#   on two functions which produces a third
#   in cv, we use kernels to specify the size
#   over our image to conduct the function

# Blurring is averaging the pixel values in a region (kernel)
import cv2, numpy as np
from google.colab.patches import cv2_imshow

image = cv2.imread('elephant.jpg')
cv2_imshow(image)

# create the 3x3 kernel
kernel_3x3 = np.ones((3,3), np.float32) / 9

blurred = cv2.filter2D(image, -1, kernel_3x3)
cv2_imshow(blurred)

# 7x7 kernel blurring
kernel_7x7 = np.ones((7,7), np.float32) / 49

blurred = cv2.filter2D(image, -1, kernel_7x7)
cv2_imshow(blurred)

# Other blur methods
import cv2, numpy as np
from google.colab.patches import cv2_imshow

image = cv2.imread('elephant.jpg')

#blur = cv2.blur(image, (3,3))
#cv2_imshow(blur)

# guassian kernel
#Gaussian = cv2.GaussianBlur(image, (7,7), 0)
#cv2_imshow(Gaussian)

# median under the kernel
#median = cv2.medianBlur(image, 5)
#cv2_imshow(median)

# bilateral is very effective in noise removel
#   while keeping edges sharp
bilateral = cv2.bilateralFilter(image, 0, 75, 75)
cv2_imshow(bilateral)

# Sharpening is the opposite of blurring, where the kernel strengthens the outside and the edges
import cv2, numpy as np
from google.colab.patches import cv2_imshow

image = cv2.imread('input.jpg')

kernel_sharpening = np.array([[-1,-1,-1],
                              [-1,9,-1],
                             [-1,-1,-1]])

sharpened = cv2.filter2D(image, -1, kernel_sharpening)
cv2_imshow(sharpened)


# Thresholding or Binarization is converting an image to a binary form
#   images need to be converted to grayscale prior to thresholding
#   it converts grayscale to simply black and white

import cv2, numpy as np
from google.colab.patches import cv2_imshow

# import image as grayscale (,0)
image = cv2.imread('gradient.jpg', 0)

# this threshold sets values below 127 to 0 (black)
# ret here is a necessary holdover from C++ syntax
ret,thresh_binary = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
cv2_imshow(thresh_binary)



# Dialition adds pixels to the boundaries of objects
# Erosion subtracts pixels to the bounderies of objects
# BOTH actually have a counter-intuative, opposite effect
import cv2, numpy as np
from google.colab.patches import cv2_imshow

image = cv2.imread('opencv_inv.png')

#define the kernel
kernel = np.ones((5,5), np.uint8)

erosion = cv2.erode(image,kernel, iterations = 1)
cv2_imshow(erosion)


# Dilation
dilation = cv2.dilate(image, kernel)
cv2_imshow(dilation)
cv2_imshow(image)

# Morphology (Opening or Closing) is good for removing noise
opening = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
cv2_imshow(opening)

######## Adjusting pixel count with resize

import cv2, numpy as np
from google.colab.patches import cv2_imshow

image = cv2.imread('favicon-32x32.png', cv2.IMREAD_UNCHANGED)
cv2.resize(image, (48,48), interpolation = cv2.INTER_AREA)
cv2.imwrite('new_favicon.png', image)

##### Edge Detection and Gradients
import cv2, numpy as np
from google.colab.patches import cv2_imshow

image = cv2.imread('input.jpg' , 0)
height, width = image.shape

# Extract Sobel edges
sobel_x = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize = 5)
sobel_y = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize = 5)

cv2_imshow(sobel_y)
cv2_imshow(sobel_x)

# Canny edge detection
canny = cv2.Canny(image,10,180)
cv2_imshow(canny)


##### Perspective Transform
import cv2, numpy as np
from google.colab.patches import cv2_imshow

image = cv2.imread('scan.jpg')

# Coordinates of the four corners in original
points_A = np.float32([[320,15], [700,215], [85,610], [530,700]])

# Coordinates of desired transform
points_B = np.float32([[0,0], [420,0], [0,594], [420,594]])

M = cv2.getPerspectiveTransform(points_A,points_B)

warped = cv2.warpPerspective(image, M, (420,594))

cv2_imshow(warped)

