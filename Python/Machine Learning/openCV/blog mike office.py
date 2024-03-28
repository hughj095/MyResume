import cv2, numpy as np
from google.colab.patches import cv2_imshow

image = cv2.imread('officemike.jpg')
face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
faces = face_classifier.detectMultiScale(gray, 1.9, 2)

for (x,y,w,h) in faces:
  cv2.rectangle(image, (x,y), (x+w, y+h), (0,255,255), 2)
  cv2.rectangle(image, (x+20,y+20), (x+20+w+20, y+20+h+20), (0,0,139), 2)
  # Define the coordinates for the label box
  x1, y1 = 586, 135  # Top-left corner
  x2, y2 = 686, 175  # Bottom-right corner

  # Define the text and its position
  text = "Happy"
  text2 = "Distressed"
  text_position = (x1 + 5, y1 + 30)  # Adjust the position for the text
  text_position2 = (x1 + 148, y1 + 238)
  cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 255), thickness=cv2.FILLED)
  cv2.rectangle(image, (x1+140, y1+210), (x2+210, y2+210), (0,0,139), thickness=cv2.FILLED)

  # Add the yellow text
  font = cv2.FONT_HERSHEY_SIMPLEX
  font_scale = 1.0
  font_color = (0, 0, 0)  
  font_color2 = (0, 255, 255)  
  font_thickness = 2

  cv2.putText(image, text, text_position, font, font_scale, font_color, font_thickness)
  cv2.putText(image, text2, text_position2, font, font_scale, font_color2, font_thickness)
  cv2_imshow(image)
