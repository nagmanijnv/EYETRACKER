import sys
import cv2
import numpy as np

image_path = 'Srikar1.jpg'
cascade_path = '/usr/share/OpenCV/haarcascades/haarcascade_frontalface_default.xml'

face_cascade = cv2.CascadeClassifier(cascade_path)

img = cv2.imread(image_path)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.1, 5, 0)

for (x, y, w, h) in faces:
	cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv2.imshow("faces", img)
k = cv2.waitKey(0) & 0xFF
if k == 27:
    cv2.distroyAllWindows()
