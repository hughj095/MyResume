###### Face and eye detection
import cv2, numpy as np
from google.colab.patches import cv2_imshow

# point classifer to the haarcascade xml and detect face and eyes in image
face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_classifier = cv2.CascadeClassifier('haarcascade_eye.xml')

image = cv2.imread('Trump.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# detect the face
faces = face_classifier.detectMultiScale(gray, 1.3, 5)

if faces is ():
  print("No faces found")

for (x,y,w,h) in faces:
  cv2.rectangle(image, (x,y), (x+w, y+h), (127, 0, 255), 2)
  cv2_imshow(image)
  roi_gray = gray[y:y+h, x:x+w]
  roi_color = image[y:y+h, x:x+w]
  eyes = eye_classifier.detectMultiScale(roi_gray)
  for (ex,ey,ew,eh) in eyes:
    cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(255,255,0),2)
    cv2_imshow(image)


######## detect face and eyes in webcam
face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_classifier = cv2.CascadeClassifier('haarcascade_eye.xml')

def face_detector(img, size=0.5):
  #convert img to grayscale
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  faces = face_classifier.detectMultiScale(gray, 1.3, 5)
  if faces is ():
    return img

  for (x,y,w,h) in faces:
    x = x - 50
    w = w + 50
    y = y - 50
    h = h + 50
    # coordinates of face
    cv2.rectangle(img, (x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = image[y:y+h, x:x+w]
    eyes = eye_classifier.detectMultiScale(roi_gray)
    
    # draw a rectangle over the color image eyes where eyes are found 
    #   in the grayscale image 
    for (ex,ey,ew,eh) in eyes:
      cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,0,255), 2)
  
  roi_color = cv2.flip(roi_color,1)
  return roi_color

cap = cv2.VideoCapture(0)

while True:

  ret, frame = cap.read()
  # imshow with function with input as video capture
  cv2_imshow(face_detector(frame))
  