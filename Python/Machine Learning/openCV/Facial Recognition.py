### This file collects webcam images, trains a model on your face, then predicts with a confidence value if a webcam face is your face with facial recognition

import cv2, numpy as np
from google.colab.patches import cv2_imshow

### Collect data on your face using webcam

face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# return cropped face
def face_extractor(img):
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  faces = face_classifier.detectMultiScale(gray, 1.3, 5)
  if faces is ():
    return None
  for (x,y,w,h) in faces:
    cropped_face = img[y:y+h, x:x+w]
  return cropped_face

# initialize webcam
cap = cv2.VideoCapture(0)
count = 0

# collect 100 samples of webcam images
while True:
  ret, frame = cap.read()
  if face_extractor(frame) is not None:
    count += 1
    face = cv2.resize(face_extractor(frame), (200,200))
    face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

    #save file with unique name
    file_name_path = './faces/user/' + str(count) + '.jpg'
    cv2.imwrite(file_name_path, face)

    # put count on images
    cv2.putText(face, str(count), (50,50), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)
    cv2_imshow(face)

else:
  print("face not found")
  pass

print("Collecting Samples Complete"
)

#### Train the model on your webcam images

from os import listdir
from os.path import isfile, join

# get training data that was collected
data_path = './faces/user/'
onlyfiles = [f for f in listdir(data_path) if isFile(join(data_path), f)]

# create arrays for data and labels
Training_Data, Labels = [], []

# append images as array to Training_Data
for i, files in enumerate(onlyfiles):
  image_path = data_path + onlyfiles[i]
  images = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
  Training_Data.append(np.asarray(images, dtype=np.uint8))
  Labels.append(i)

# Append labels as array to Labels
Labels = np.asarray(Labels, dtype=np.int32)

# make variable for model
model = cv2.createLBPHFaceRecognizer()

# train the model
model.train(np.asarray(Training_Data), np.asarray(Labels))
print("model trained")







# Run Facial Recognition

face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

def face_detector(img, size=0.5)
  # convert to grayscale
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  face = face_classifer.detectMultiScale(gray, 1.3, 5)
  if faces is ():
    return img, []
  
  for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y), (x+w,y+h), (0,255,255),2)
    roi = img[y:y+h, x:x+w]
    roi = cv2.resize(roi, (200,200))
  return img, roi

# open webcam
cap = cv2.VideoCapture(0)

while True:
  ret, frame = cap.read()

  image, face = face_detector(frame)

  try:
    face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

    # pass face to prediction model
    # results in a tuple containing the label and the confidence value as a number
    results = model.predict(face)

    # results[1] is the second value of 2, or the confidence value
    if results[1] < 500:
      # confidence calculates a percentage value
      confidence = int( 100 * (1 - (results[1])/300))
      display_string = str(confidence) + '% Confident it is User'

    cv2.putText(image, display_string, (100, 120), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 120, 150), 2)

    if confidence > 75:
      cv2.putText(image, "Unlocked", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)
      cv2_imshow(image)
    else:
      cv2.putText(image, "Locked", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)
      cv2_imshow(image)

  except:
    cv2.putText(image, "No face found", (220,120), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0,0,255), 2)
    cv2.putText(image, "Locked", (220,120), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0,0,255), 2)
    cv2_imshow(image)


      









# Run Facial Recognition


