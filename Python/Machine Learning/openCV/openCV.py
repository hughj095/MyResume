import cv2
import numpy as np
from google.colab.patches import cv2_imshow

# Load an image using 'imread' specifying the path to image
input = cv2.imread('input.jpg')
print(input.shape)

print('Height of Image', int(input.shape[0]), 'pixels')

# 'waitKey' allows us to input information when a image window is open
# By leaving it blank it just waits for anykey to be pressed before
# continuing. By placing numbers (except 0), we can specify a delay for
# how long you keep the window open (time is in milliseconds here)
cv2.waitKey()

# This closes all open windows
# Failure to place this will cause your program to hang
cv2.destroyAllWindows()


### How do we save images we edit in OpenCV?
# Simply use 'imwrite' specificing the file name and the image to be saved
cv2.imwrite('output.jpg', input)
cv2.imwrite('output.png', input)

# Convert image to grayscale
gray_image = cv2.cvtColor(input, cv2.COLOR_BGR2GRAY)
# This method also works
img = cv2.imread('input.jpg',0)
print(img.shape)
cv2.imwrite('gray.png',img)

# HSV is Hue, Saturation, Value/Brightness
# CMYK is for printers, Cyan, Magenta, Yellow, Black
# RGB is stored as BGR actually, Blue Green Red
# Hue is 0-179, while Saturation and Value is 0-255

B,G,R = input[10,50]
print(B,G,R)
print(input.shape)
img = cv2.imread('input.jpg',0)
print(img[10,0])

# use the cvt function to access HSV values
hsv_image = cv2.cvtColor(input, cv2.COLOR_BGR2HSV)
# substitute 0 hue for 1 (saturation) or 2 (value)
cv2_imshow(hsv_image[:,:,0])
cv2.imwrite('output.jpg', hsv_image)


# Split the image into blue, green and red, then merge them back
B,G,R = cv2.split(input)
cv2.imwrite('G.jpg', G)
merged = cv2.merge([B,G,R])
cv2.imwrite('assemble.jpg', merged)
#amplify the Blue
merged = cv2.merge([B+100, G, R])
cv2_imshow(merged)

#Isolate the zeros in the arrays to show only red
B,G,R = cv2.split(input)
zeros = np.zeros(input.shape[:2], dtype = "uint8")
cv2_imshow(cv2.merge([zeros,zeros,R]))

# Histograms of pixel colors
from matplotlib import pyplot as plt

histogram = cv2.calcHist([input], [0], None, [256], [0,256])

#Viewing all colors as one histogram
plt.hist(input.ravel(), 256, [0,256]); plt.show()

#View as seperate channels
color = ('b','g','r')

for i, col in enumerate(color):
  histogram2 = cv2.calcHist([input], [i], None, [256], [0,256])
  plt.plot(histogram2, color = col)
  plt.xlim([0,256])
plt.show()

# Create a black image
import cv2
import numpy as np

input = np.zeros((512,512,3), np.uint8)

# Make black and white by taking out 3rd dimension (but they look identical)
input = np.zeros((512,512), np.uint8)

cv2_imshow(input)

# Draw a diagonal blue line
image = np.zeros((512,512,3), np.uint8)
# inputs below are file, start point, end point, color, thickness
cv2.line(image, (0,0), (511,511), (255,127,0), 5)
cv2_imshow(image)

# Draw a rectangle
image = np.zeros((512,512,3), np.uint8)
# inputs below are file, start point, end point, color, thickness
cv2.rectangle(image, (100,100), (300,250), (127,50,127), 5)
cv2_imshow(image)
# a thickness of -1 fills in the rectangle
cv2.rectangle(image, (100,100), (300,250), (127,50,127), -1)
cv2_imshow(image)

# Circle cv2.circle arguments are center and radius, color, thickness

# A polygon
# define the four points
pts = np.array([[10,50], [400,50], [90,200], [50,500]], np.int32)
pts = pts.reshape((-1,1,2))

cv2.polylines(image, [pts], True, (0,255,0), 5)
cv2_imshow(image)

#putText
image = np.zeros((512,512,3), np.uint8)

cv2.putText(image, "Hello World", (75,290), cv2.FONT_HERSHEY_COMPLEX, 2, (100, 170,0), 3)
cv2_imshow(image)

